from typing import List
from datetime import datetime, timedelta
from ..models.base import ApiObject

class AdditionalFeesResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "additionalfees"
    
    def update(self, request: ApiObject) -> ApiObject:
        """
        Update additional fees for a campaign or ad group.
        """
        
        if not self._is_valid_start_date(datetime.fromisoformat(request.StartDateUtc)):
            raise ValueError("Start date must be at least one hour in the future")
        
        response = self.client.put(self.base_path, request.to_dict())
        return ApiObject(**response)
    
    def _is_valid_start_date(self, start_date: datetime) -> bool:
        time_difference = start_date - datetime.utcnow()
        return time_difference.total_seconds() >= 3600
    
    def get(self, owner_type: str, owner_id: str) -> ApiObject:
        """
        Get the current fee card for a campaign or ad group.
        
        Args:
            owner_type: Either "adgroup" or "campaign"
            owner_id: The ID of the owner entity
        """
        if owner_type not in ["adgroup", "campaign"]:
            raise ValueError('owner_type must be either "adgroup" or "campaign"')
        
        response = self.client.get(f"{self.base_path}/{owner_type}/{owner_id}")
        return ApiObject(**response)
    
    def create(
        self,
        owner_type: str,
        owner_id: str,
        fees: List[ApiObject],
        start_date: datetime = None
    ) -> ApiObject:
        """
        Create a new fee card for a campaign or ad group.
        
        Args:
            owner_type: Either "adgroup" or "campaign"
            owner_id: The ID of the owner entity
            fees: List of fee dictionaries, each containing Amount, Description, and FeeType
            start_date: When the fees should take effect (defaults to 2 hours from now)
        
        Returns:
            ApiObject: The created fee card
        """
        if owner_type not in ["adgroup", "campaign"]:
            raise ValueError('owner_type must be either "adgroup" or "campaign"')
        
        if start_date is None:
            start_date = datetime.utcnow() + timedelta(hours=1.1)
        
        if not self._is_valid_start_date(start_date):
            raise ValueError("Start date must be at least one hour in the future")
        
        request = ApiObject(
            Fees=fees,
            OwnerId=owner_id,
            OwnerType=owner_type,
            StartDateUtc=start_date.isoformat()
        )
        
        response = self.client.post(self.base_path, request.to_dict())
        return ApiObject(**response)
    
    def add_fee(
        self, 
        owner_type: str, 
        owner_id: str, 
        new_fee: ApiObject,  # Change type hint to ApiObject
        start_date: datetime = None,
        *, 
        prevent_duplicates: bool = True
    ) -> ApiObject:
        """
        Add a single fee while preserving existing fees.
        Creates a new fee card if none exists, otherwise adds to existing card.
        
        Args:
            owner_type: Either "adgroup" or "campaign"
            owner_id: The ID of the owner entity
            new_fee: ApiObject containing Amount, Description, and FeeType
            start_date: When the fee should take effect (defaults to 2 hours from now)
            prevent_duplicates: If True, raises ValueError if description already exists
        """
        if start_date is None:
            start_date = datetime.utcnow() + timedelta(hours=1.1)
        
        if not self._is_valid_start_date(start_date):
            raise ValueError("Start date must be at least one hour in the future")
        
        # Get the owner entity
        if owner_type == "campaign":
            response = self.client.campaigns.get(owner_id)
        else:
            response = self.client.ad_groups.get(owner_id)
        
        # Check for existing fee cards
        has_fee_cards = (
            hasattr(response, 'CurrentAndFutureAdditionalFeeCards') and 
            len(response.CurrentAndFutureAdditionalFeeCards) > 0
        )
        
        if has_fee_cards:
            # Get most recent fee card
            sorted_cards = sorted(
                response.CurrentAndFutureAdditionalFeeCards,
                key=lambda x: x.StartDateUtc,
                reverse=True
            )
            future_fees = sorted_cards[0].Fees
            
            # Check for duplicate description
            if prevent_duplicates and any(
                fee.Description == new_fee.Description  # Use dot notation
                for fee in future_fees
            ):
                raise ValueError(
                    f"Fee with description '{new_fee.Description}' "  # Use dot notation
                    f"already exists for {owner_type} {owner_id}"
                )
                
            # Add to existing fee card
            request = ApiObject(
                Fees=future_fees + [new_fee],  # Pass ApiObject directly
                OwnerId=owner_id,
                OwnerType=owner_type,
                StartDateUtc=start_date.isoformat()
            )
            return self.update(request)
        else:
            # Create new fee card
            return self.create(
                owner_type=owner_type,
                owner_id=owner_id,
                fees=[new_fee],  # Pass ApiObject directly
                start_date=start_date
            )
    
    def rename_fee(
        self,
        owner_type: str,
        owner_id: str,
        old_description: str,
        new_description: str,
        start_date: datetime = None
    ) -> ApiObject:
        """
        Rename a fee while preserving all other fees.
        
        Args:
            owner_type: Either "adgroup" or "campaign"
            owner_id: The ID of the owner entity
            old_description: Current description of the fee to rename
            new_description: New description for the fee
            start_date: When the change should take effect (defaults to 2 hours from now)
            
        Returns:
            ApiObject: The updated fee card
            
        Raises:
            ValueError: If the old description doesn't exist or if new description already exists
        """
        if owner_type not in ["adgroup", "campaign"]:
            raise ValueError('owner_type must be either "adgroup" or "campaign"')

        if start_date is None:
            start_date = datetime.utcnow() + timedelta(hours=1.1)

        if not self._is_valid_start_date(start_date):
            raise ValueError("Start date must be at least one hour in the future")

        # Get the owner entity
        if owner_type == "campaign":
            response = self.client.campaigns.get(owner_id)
        else:
            response = self.client.ad_groups.get(owner_id)

        # Check for existing fee cards
        if not hasattr(response, 'CurrentAndFutureAdditionalFeeCards') or \
           len(response.CurrentAndFutureAdditionalFeeCards) == 0:
            raise ValueError(f"No fee cards found for {owner_type} {owner_id}")

        # Get most recent fee card
        sorted_cards = sorted(
            response.CurrentAndFutureAdditionalFeeCards,
            key=lambda x: x.StartDateUtc,
            reverse=True
        )
        current_fees = sorted_cards[0].Fees

        # Find the fee to rename
        fee_to_rename = None
        updated_fees = []
        
        for fee in current_fees:
            if fee.Description == old_description:
                fee_to_rename = fee
                # Check if new name already exists
                if any(f.Description == new_description for f in current_fees):
                    raise ValueError(
                        f"Fee with description '{new_description}' already exists"
                    )
                # Update description and add to list
                fee.Description = new_description
                updated_fees.append(fee)
            else:
                updated_fees.append(fee)

        if fee_to_rename is None:
            raise ValueError(
                f"Fee with description '{old_description}' not found"
            )

        # Create update request
        request = ApiObject(
            Fees=updated_fees,
            OwnerId=owner_id,
            OwnerType=owner_type,
            StartDateUtc=start_date.isoformat()
        )
        
        return self.update(request)
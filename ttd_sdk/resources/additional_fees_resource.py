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
    
    def add_fee(
        self, 
        owner_type: str, 
        owner_id: str, 
        new_fee: dict, 
        start_date: datetime = None
    ) -> ApiObject:
        """
        Add a single fee while preserving existing fees.
        
        Args:
            owner_type: Either "adgroup" or "campaign"
            owner_id: The ID of the owner entity
            new_fee: Dictionary containing Amount, Description, and FeeType
            start_date: When the fee should take effect (defaults to 2 hours from now)
        """
        if start_date is None:
            start_date = datetime.utcnow() + timedelta(hours=2)
        
        if not self._is_valid_start_date(start_date):
            raise ValueError("Start date must be at least one hour in the future")
        
        if owner_type == "campaign":
            response = self.client.campaigns.get(owner_id)
        else:
            response = self.client.ad_groups.get(owner_id)
        
        future_fees = []
        if hasattr(response, 'CurrentAndFutureAdditionalFeeCards'):
            sorted_cards = sorted(
                response.CurrentAndFutureAdditionalFeeCards,
                key=lambda x: x.StartDateUtc,
                reverse=True
            )
            if sorted_cards:
                future_fees = sorted_cards[0].Fees
        
        request = ApiObject(
            Fees=future_fees + [new_fee],
            OwnerId=owner_id,
            OwnerType=owner_type,
            StartDateUtc=start_date.isoformat()
        )
        
        return self.update(request)
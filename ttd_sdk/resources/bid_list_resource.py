from typing import Iterator, Optional, List, Dict
import time
from ..models.base import ApiObject

class BidListResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "bidlist"
    
    def create(self, bid_list: ApiObject) -> ApiObject:
        """
        Create a new bid list.
        
        Notes:
            - All BidLines must set the same properties (except BidAdjustment)
            - BidListAdjustmentType cannot be changed after creation
            - ResolutionType is required for Optimized lists, defaults to ApplyMultiplyAdjustment for Target/Block lists
            - IsAvailableForLibraryUse cannot be true for AdGroup-owned lists
        """
        if not getattr(bid_list, 'Name', None):
            raise ValueError("Name is required (max 512 characters)")
            
        if not getattr(bid_list, 'BidListAdjustmentType', None):
            raise ValueError("BidListAdjustmentType is required")
            
        if not getattr(bid_list, 'BidLines', None):
            raise ValueError("BidLines is required")
            
        if len(bid_list.BidLines) > 1:
            first_line = bid_list.BidLines[0]
            first_line_fields = {k for k, v in first_line.to_dict().items() 
                               if k != "BidAdjustment"}
            
            for line in bid_list.BidLines[1:]:
                line_fields = {k for k, v in line.to_dict().items() 
                             if k != "BidAdjustment"}
                if line_fields != first_line_fields:
                    raise ValueError(
                        "All bid lines must set the same properties (except BidAdjustment)"
                    )
        
        if (bid_list.BidListAdjustmentType == "Optimized" 
            and not getattr(bid_list, 'ResolutionType', None)):
            raise ValueError("ResolutionType is required for Optimized bid lists")
            
        data = bid_list.to_dict()
        response = self.client.post(self.base_path, data)
        return ApiObject(**response)
    
    def get(self, bid_list_id: str) -> ApiObject:
        """
        Retrieve the content of a bid list including all bid dimension line items.
        """
        response = self.client.get(f"{self.base_path}/{bid_list_id}")
        return ApiObject(**response)
    
    def update(self, bid_list_id: str, bid_list: ApiObject) -> ApiObject:
        """
        Update an existing bid list.
        """
        data = bid_list.to_dict()
        response = self.client.put(f"{self.base_path}", data)  # Remove ID from path
        return ApiObject(**response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 100,
        bid_list_ids: Optional[List[int]] = None,
        dimension_descriptor_filters: Optional[List[str]] = None,
        maximum_level: Optional[str] = None,
        return_unavailable_for_library_use: bool = False,
        return_only_enabled_bid_lists: bool = False,
    ) -> Iterator[ApiObject]:
        data = {
            "EntityId": advertiser_id,
            "ReturnBidListsUnavailableForLibraryUse": return_unavailable_for_library_use,
            "ReturnOnlyEnabledBidLists": return_only_enabled_bid_lists
        }
        
        if bid_list_ids:
            data["BidListIds"] = bid_list_ids
        if dimension_descriptor_filters:
            data["DimensionDescriptorFilters"] = dimension_descriptor_filters
        if maximum_level:
            data["MaximumLevel"] = maximum_level
            
        for result in self.client.post_with_pagination(
            "bidlistsummary/query/advertiser/available",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
    
    def list_by_ad_group(
        self,
        ad_group_id: str,
        page_size: int = 100,
        bid_list_ids: Optional[List[int]] = None,
        dimension_descriptor_filters: Optional[List[str]] = None,
        maximum_level: Optional[str] = None,
        return_unavailable_for_library_use: bool = False,
        return_only_enabled_bid_lists: bool = False,
    ) -> Iterator[ApiObject]:
        """
        Retrieve bid lists available to associate with an ad group.
        """
        data = {
            "EntityId": ad_group_id,
            "ReturnBidListsUnavailableForLibraryUse": return_unavailable_for_library_use,
            "ReturnOnlyEnabledBidLists": return_only_enabled_bid_lists
        }
        
        if bid_list_ids:
            data["BidListIds"] = bid_list_ids
        if dimension_descriptor_filters:
            data["DimensionDescriptorFilters"] = dimension_descriptor_filters
        if maximum_level:
            data["MaximumLevel"] = maximum_level
        
        for result in self.client.post_with_pagination(
            "bidlistsummary/query/adgroup/available",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
    
    def batch_get(self, bid_list_ids: List[str]) -> Dict[str, ApiObject]:
        """
        Retrieve multiple bid lists in a single request. Automatically handles batching for lists longer than 20 ids.
        Includes a 1-second delay between batch requests to prevent resource exhaustion.
        """
        BATCH_SIZE = 20
        results = {}
        
        total_batches = (len(bid_list_ids) + BATCH_SIZE - 1) // BATCH_SIZE
        
        for i in range(0, len(bid_list_ids), BATCH_SIZE):
            batch = bid_list_ids[i:i + BATCH_SIZE]
            response = self.client.post(f"{self.base_path}/batch/get", batch)
            
            batch_results = response.get("BatchResponses", {})
            results.update(batch_results)
            
            # Add delay if this isn't the last batch
            if i + BATCH_SIZE < len(bid_list_ids):
                time.sleep(1)
        
        return {
            bid_list_id: ApiObject(**bid_list_data)
            for bid_list_id, bid_list_data in results.items()
        }

    def delete(self, bid_list_id: str) -> None:
        """
        Delete a bid list and its associations.

        Args:
            bid_list_id: The ID of the bid list to delete
        """
        self.client.delete(f"{self.base_path}/{bid_list_id}")

    def list_unassociated(
        self,
        partner_id: str,
        owner_entity_type: str,
        page_size: int = 100,
        page_start_index: int = 0
    ) -> Iterator[ApiObject]:
        """
        Retrieve a paged list of unassociated bid lists at a given level of ownership.

        Args:
            partner_id: The ID of the partner making the query
            owner_entity_type: The entity type (AdGroup, Campaign, Advertiser, or Partner)
                             whose unassociated bid lists are to be included
            page_size: Number of items per page (max 1000, default 100)
            page_start_index: Zero-based index for pagination start (default 0)

        Yields:
            ApiObject: Unassociated bid lists matching the query criteria
        """
        if page_size > 1000:
            raise ValueError("Maximum page size is 1000")

        data = {
            "PartnerId": partner_id,
            "OwnerEntityType": owner_entity_type,
            "PageSize": page_size,
            "PageStartIndex": page_start_index
        }

        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/unassociated",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)

    def list_associated(
        self,
        bid_list_id: str,
        page_size: int = 1000,
        page_start_index: int = 0,
        return_ad_groups: bool = False,
        return_campaigns: bool = False,
        return_advertisers: bool = False,
        return_partners: bool = False,
        return_enabled_only: bool = False
    ) -> Iterator[ApiObject]:
        """
        Retrieve a paged list of entities associated with a specific bid list.

        Args:
            bid_list_id: The ID of the bid list to query
            page_size: Number of items per page (max 10000, default 1000)
            page_start_index: Zero-based index for pagination start (default 0)
            return_ad_groups: Include associated ad groups in response
            return_campaigns: Include associated campaigns in response
            return_advertisers: Include associated advertisers in response
            return_partners: Include associated partners in response
            return_enabled_only: Only return enabled associations if True

        Yields:
            ApiObject: Associated entities matching the query criteria

        Raises:
            ValueError: If page_size exceeds 1000 or no entity types are selected for return
        """
        if page_size > 1000:
            raise ValueError("Maximum page size is 1000")

        if not any([return_ad_groups, return_campaigns, return_advertisers, return_partners]):
            raise ValueError(
                "At least one entity type must be selected "
                "(ad_groups, campaigns, advertisers, or partners)"
            )

        data = {
            "BidListId": bid_list_id,
            "PageSize": page_size,
            "PageStartIndex": page_start_index,
            "ReturnAssociatedAdGroups": return_ad_groups,
            "ReturnAssociatedCampaigns": return_campaigns,
            "ReturnAssociatedAdvertisers": return_advertisers,
            "ReturnAssociatedPartners": return_partners,
            "ReturnEnabledAssociationOnly": return_enabled_only
        }

        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/associated",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
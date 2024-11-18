from typing import Iterator, Optional, List, Dict
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
        
        Notes:
            - BidListAdjustmentType cannot be changed after creation
            - When changing owner, new owner must be an ancestor of previous owner
        """
        if getattr(bid_list, 'BidListAdjustmentType', None):
            raise ValueError("BidListAdjustmentType cannot be changed after creation")
            
        data = bid_list.to_dict()
        response = self.client.put(f"{self.base_path}/{bid_list_id}", data)
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
        """Retrieve multiple bid lists in a single request."""
        response = self.client.post(f"{self.base_path}/batch/get", bid_list_ids)
            
        results = {}
        for bid_list_id, bid_list_data in response.get("BatchResponses", {}).items():
            results[bid_list_id] = ApiObject(**bid_list_data)
            
        return results
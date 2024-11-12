from typing import Iterator, Optional, Dict, Any, List
from ..models.data_group import DataGroup

class DataGroupResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "datagroup"
    
    def create(self, data_group: DataGroup) -> DataGroup:
        """
        Create a new data group.
        """
        if not data_group.data_group_name or not data_group.advertiser_id:
            raise ValueError("data_group_name and advertiser_id are required")
        
        data = data_group.model_dump(exclude_none=True)
        response = self.client.post(self.base_path, data)
        return DataGroup.model_validate(response)
    
    def get(self, data_group_id: str) -> DataGroup:
        """
        Get a data group by ID.
        """
        response = self.client.get(f"{self.base_path}/{data_group_id}")
        return DataGroup.model_validate(response)
    
    def update(self, data_group_id: str, data_group: DataGroup) -> DataGroup:
        """
        Update an existing data group.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = data_group.model_dump(exclude_none=True)
        response = self.client.put(f"{self.base_path}/{data_group_id}", data)
        return DataGroup.model_validate(response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 100,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[DataGroup]:
        """
        Get a paginated list of data groups for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            search_terms: Optional list of search terms to filter by
            sort_fields: Optional list of sort field configurations
        """
        data = {"AdvertiserId": advertiser_id}
        
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/advertiser",
            data=data,
            page_size=page_size
        ):
            yield DataGroup.model_validate(result)
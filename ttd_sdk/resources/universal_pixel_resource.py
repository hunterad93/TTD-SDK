from typing import Iterator, Optional, Dict, Any, List
from ..models.universal_pixel import UniversalPixel, UniversalPixelCode

class UniversalPixelResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "tracking/universalpixel"
    
    def create(self, pixel: UniversalPixel) -> UniversalPixel:
        """
        Create a new universal pixel.
        """
        if not pixel.universal_pixel_name or not pixel.advertiser_id:
            raise ValueError("universal_pixel_name and advertiser_id are required")
        
        data = pixel.model_dump(exclude_none=True)
        response = self.client.post(self.base_path, data)
        return UniversalPixel.model_validate(response)
    
    def get(self, pixel_id: str) -> UniversalPixel:
        """
        Get a universal pixel by ID.
        """
        response = self.client.get(f"{self.base_path}/{pixel_id}")
        return UniversalPixel.model_validate(response)
    
    def update(self, pixel_id: str, pixel: UniversalPixel) -> UniversalPixel:
        """
        Update an existing universal pixel.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = pixel.model_dump(exclude_none=True)
        response = self.client.put(f"{self.base_path}/{pixel_id}", data)
        return UniversalPixel.model_validate(response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 100,  # Max page size is 100 for this endpoint
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[UniversalPixel]:
        """
        Get a paginated list of universal pixels for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (max 100)
            sort_fields: Optional list of sort field configurations
        """
            
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}withactivity/advertiser/query",
            data=data,
            page_size=page_size
        ):
            yield UniversalPixel.model_validate(result)
    
    def get_pixel_code(self, pixel_id: str) -> UniversalPixelCode:
        """
        Get the pixel code for a universal pixel.
        """
        response = self.client.get(f"{self.base_path}/{pixel_id}/code")
        return UniversalPixelCode.model_validate(response) 
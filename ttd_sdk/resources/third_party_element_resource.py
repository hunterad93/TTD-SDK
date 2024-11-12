from typing import Iterator, Optional, Dict, Any, List
from ..models.third_party_element import ThirdPartyElement, ThirdPartyBrand

class ThirdPartyElementResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "dmp/thirdparty"
    
    def get(self, element_id: str, advertiser_id: str) -> ThirdPartyElement:
        """
        Get details of a specific third party data element.
        """
        elements = list(self.list(
            advertiser_id=advertiser_id,
            third_party_data_ids=[element_id],
            page_size=1000
        ))
        if not elements:
            raise ValueError(f"No element found with ID {element_id}")
        return elements[0]
    
    def list_by_brand(
        self,
        brand_id: str,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ThirdPartyElement]:
        """
        Get a paginated list of third party data elements for a specific brand.
        """
        return self.list(
            advertiser_id=advertiser_id,
            brand_ids=[brand_id],
            page_size=page_size,
            sort_fields=sort_fields
        )
    
    def list(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        brand_ids: Optional[List[str]] = None,
        third_party_data_ids: Optional[List[str]] = None,
        search_terms: Optional[List[str]] = None,
    ) -> Iterator[ThirdPartyElement]:
        """
        Get a paginated list of third party data elements with optional filtering.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            brand_ids: Optional list of brand IDs to filter by
            third_party_data_ids: Optional list of specific third party data IDs
            search_terms: Optional list of search terms to filter by
        """
        if page_size < 100 or page_size > 1000:
            raise ValueError("page_size must be between 100 and 1000")
            
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if brand_ids:
            data["BrandIds"] = brand_ids
        if third_party_data_ids:
            data["ThirdPartyDataIds"] = third_party_data_ids
        if search_terms:
            data["SearchTerms"] = search_terms
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/advertiser",
            data=data,
            page_size=page_size
        ):
            yield ThirdPartyElement.model_validate(result)
    
    def get_available_brands(self, advertiser_id: str) -> List[ThirdPartyBrand]:
        """
        Get a list of third party data brands available to an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
        """
        response = self.client.get(f"{self.base_path}/facets/{advertiser_id}")
        return [ThirdPartyBrand.model_validate(brand) for brand in response["Brands"]]
    
    def bulk_third_party_query(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ThirdPartyElement]:
        """
        Get all third party data elements across all available brands for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
        """
        # First get all available brand IDs
        brands = self.get_available_brands(advertiser_id)
        brand_ids = [brand.brand_id for brand in brands if brand.brand_id]
        
        if not brand_ids:
            return iter([])  # Return empty iterator if no brands available
        
        # Use the list method with all brand IDs
        return self.list(
            advertiser_id=advertiser_id,
            brand_ids=brand_ids,
            page_size=page_size,
            sort_fields=sort_fields
        )
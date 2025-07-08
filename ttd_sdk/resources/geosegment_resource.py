from typing import Iterator, Optional, Dict, List
from ..models.base import ApiObject

class GeoSegmentResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "geosegment"
    
    def list_by_partner(
        self,
        page_size: int = 1000,
        page_start_index: int = 0,
        geo_segment_filter: str = "All",
        partner_id: Optional[str] = None,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get a paginated list of geo segments available for a partner.
        
        Args:
            page_size: Number of results per page (100-1000 recommended)
            page_start_index: Zero-based index for pagination start
            geo_segment_filter: Filter type for geo segments 
                (All, CustomOnly, StandardOnly, Country, Region, City, Zip, Metro, PartnerSpecific)
            partner_id: Optional partner ID to query (uses user's primary partner ID if not specified)
            search_terms: Optional list of search terms to filter results
            sort_fields: Optional list of sort field configurations
        """
        data = {
            "PageSize": page_size,
            "PageStartIndex": page_start_index,
            "GeoSegmentFilter": geo_segment_filter
        }
        
        if partner_id:
            data["PartnerId"] = partner_id
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
            
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/partner",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)

    def get_name(self, geo_segment_id: str) -> ApiObject:
        """
        Get the identifier and name for a GeoSegment based on identifier.
        
        Args:
            geo_segment_id: The GeoSegment identifier
            
        Returns:
            ApiObject with Id and Name fields
        """
        response = self.client.get(f"{self.base_path}/name/{geo_segment_id}")
        return ApiObject(**response)
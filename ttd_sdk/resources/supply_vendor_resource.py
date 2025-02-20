from typing import Iterator, Optional, Dict, Any, List
from ..models.base import ApiObject

class SupplyVendorResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "supplyvendor"

    def list(
        self,
        partner_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        are_deals_supported: Optional[bool] = None,
        search_terms: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get a paginated list of supply vendors available to a partner.
        
        Args:
            partner_id: The ID of the Partner requesting supply vendors
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            are_deals_supported: Optional filter for vendors supporting deals
            search_terms: Optional list of search terms to filter by
        """
        if page_size < 100 or page_size > 1000:
            raise ValueError("page_size must be between 100 and 1000")
            
        data = {"PartnerId": partner_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if are_deals_supported is not None:
            data["AreDealsSupported"] = are_deals_supported
        if search_terms:
            data["SearchTerms"] = search_terms
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/partner",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)

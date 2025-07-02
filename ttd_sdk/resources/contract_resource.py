from typing import Iterator, Optional, Dict, List
from ..models.base import ApiObject

class ContractResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "contract"
    
    def get(self, contract_id: str) -> ApiObject:
        """
        Get an existing contract by ID.
        """
        response = self.client.get(f"{self.base_path}/{contract_id}")
        return ApiObject(**response)

    def list_by_partner(
        self,
        partner_id: str,
        page_size: int = 1000,
        page_start_index: int = 0,
        availabilities: Optional[List[str]] = None,
        contract_types: Optional[List[str]] = None,
        owner_partner_ids: Optional[List[str]] = None,
        return_only_ids: bool = False,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
        """
        Query for contracts available to advertisers under the chosen partner.
        
        """
        data = {
            "PartnerId": partner_id,
            "PageSize": page_size,
            "PageStartIndex": page_start_index,
            "ReturnOnlyIds": return_only_ids
        }
        
        if availabilities:
            data["Availabilities"] = availabilities
        if contract_types:
            data["ContractTypes"] = contract_types
        if owner_partner_ids:
            data["OwnerPartnerIds"] = owner_partner_ids
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
            
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/partner/available",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)

    def list_owned_by_partner(
        self,
        partner_id: str,
        page_size: int = 1000,
        page_start_index: int = 0,
        availabilities: Optional[List[str]] = None,
        contract_types: Optional[List[str]] = None,
        return_only_ids: bool = False,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
        """
        Query for contracts owned by a partner.
        
        """
        data = {
            "PartnerId": partner_id,
            "PageSize": page_size,
            "PageStartIndex": page_start_index,
            "ReturnOnlyIds": return_only_ids
        }
        
        if availabilities:
            data["Availabilities"] = availabilities
        if contract_types:
            data["ContractTypes"] = contract_types
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
            
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/partner",  # Different endpoint than list_by_partner
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
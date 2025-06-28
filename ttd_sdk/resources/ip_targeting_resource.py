from typing import Iterator, Optional, List, Dict
from ..models.base import ApiObject

class IPTargetingResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "iptargetinglist"
    
    def get_usage(self, advertiser_id: str) -> ApiObject:
        """Get the cumulative IP Targeting Lists usage for an Advertiser."""
        response = self.client.get(f"{self.base_path}/usage/{advertiser_id}")
        return ApiObject(**response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 100,
        page_start_index: int = 0,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict]] = None
    ) -> Iterator[ApiObject]:
        """Get IP Targeting Lists for an advertiser with pagination support."""
        if page_size > 1000:
            raise ValueError("Maximum page size is 1000")
        if page_size < 100 and page_size != 0:
            raise ValueError("Minimum page size is 100")
            
        data = {
            "AdvertiserId": advertiser_id,
            "PageSize": page_size,
            "PageStartIndex": page_start_index
        }
        
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
            
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/advertiser",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)

    def get(self, ip_targeting_list_id: str) -> ApiObject:
        """Get an existing IP Targeting List by ID."""
        response = self.client.get(f"{self.base_path}/{ip_targeting_list_id}")
        return ApiObject(**response)

    def update(self, ip_targeting_list_id: str, ip_targeting_list: ApiObject) -> ApiObject:
        """
        Update an IP Targeting List. Returns summary instead of full list.
        Note: IPTargetingDataName cannot be changed after creation.
        """
        data = ip_targeting_list.to_dict()
        response = self.client.put(f"{self.base_path}/{ip_targeting_list_id}", data)
        return ApiObject(**response)

    def create(self, ip_targeting_list: ApiObject) -> ApiObject:
        """
        Create a new IP Targeting List. Returns summary instead of full list.
        Requires: AdvertiserId, IPTargetingDataName, IPTargetingRanges
        """
        if not getattr(ip_targeting_list, 'AdvertiserId', None) or \
           not getattr(ip_targeting_list, 'IPTargetingDataName', None) or \
           not getattr(ip_targeting_list, 'IPTargetingRanges', None):
            raise ValueError("AdvertiserId, IPTargetingDataName, and IPTargetingRanges are required")
        
        data = ip_targeting_list.to_dict()
        response = self.client.post(self.base_path, data)
        return ApiObject(**response)

    def _create_ip_ranges(self, ip_list: List[str]) -> List[Dict[str, str]]:
        """Convert list of IPv4 addresses into minimal set of IP ranges."""
        def is_valid_ipv4(ip: str) -> bool:
            try:
                parts = ip.split('.')
                if len(parts) != 4:
                    return False
                return all(0 <= int(part) <= 255 for part in parts)
            except (AttributeError, TypeError, ValueError):
                return False

        def ip_to_int(ip: str) -> int:
            parts = [int(x) for x in ip.split('.')]
            return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]
        
        def int_to_ip(n: int) -> str:
            return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"
        
        if not ip_list:
            return []

        # Validate all IPs first
        invalid_ips = [ip for ip in ip_list if not is_valid_ipv4(ip)]
        if invalid_ips:
            raise ValueError(f"Invalid IPv4 addresses found: {invalid_ips}")
        
        # Convert to integers and sort
        ip_ints = sorted(ip_to_int(ip) for ip in ip_list)
        
        # Find ranges
        ranges = []
        range_start = ip_ints[0]
        prev = ip_ints[0]
        
        for curr in ip_ints[1:] + [None]:
            if curr is None or curr > prev + 1:
                ranges.append({
                    "MinIP": int_to_ip(range_start),
                    "MaxIP": int_to_ip(prev)
                })
                range_start = curr
            prev = curr
        
        return ranges

    def create_or_update_ip_list(
        self,
        advertiser_id: str,
        list_name: str,
        ip_addresses: List[str]
    ) -> ApiObject:
        """Create or update IP targeting list from individual IPs."""
        # Check if list exists by searching through advertiser's lists
        existing_list_id = None
        for list_summary in self.list_by_advertiser(
            advertiser_id=advertiser_id,
            search_terms=[list_name]
        ):
            if getattr(list_summary, 'IPTargetingDataName', None) == list_name:
                existing_list_id = list_summary.IPTargetingListId
                break

        # Convert IPs to ranges
        ip_ranges = self._create_ip_ranges(ip_addresses)
        
        if existing_list_id:
            # Update existing list
            return self.update(
                existing_list_id,
                ApiObject(**{
                    "AdvertiserId": advertiser_id,
                    "IPTargetingRanges": ip_ranges
                })
            )
        else:
            # Create new list
            return self.create(
                ApiObject(**{
                    "AdvertiserId": advertiser_id,
                    "IPTargetingDataName": list_name,
                    "IPTargetingRanges": ip_ranges
                })
            )

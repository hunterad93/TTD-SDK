from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .brandrestrictionissuecreative import BrandRestrictionIssueCreative


@dataclass
class BrandRestrictionIssueAdGroup:
    """
    Ad Group with Brand Restriction Issues
    """
    adGroup: Optional[AdGroup]
    brandRestrictionIssueCreatives: List[Optional[BrandRestrictionIssueCreative]]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .brandrestrictionissueadgroup import BrandRestrictionIssueAdGroup
    from .creativeissuetype import CreativeIssueType
    from .creativesconnection import CreativesConnection


@dataclass
class BrandRestrictionIssue:
    """
    None
    """
    creatives: Optional[CreativesConnection]
    issueAdGroups: List[Optional[BrandRestrictionIssueAdGroup]]
    issueType: Optional[CreativeIssueType]

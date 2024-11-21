from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativeissuetype import CreativeIssueType
    from .creativesconnection import CreativesConnection


@dataclass
class UserApprovalIssue:
    """
    None
    """
    creatives: Optional[CreativesConnection]
    issueType: Optional[CreativeIssueType]

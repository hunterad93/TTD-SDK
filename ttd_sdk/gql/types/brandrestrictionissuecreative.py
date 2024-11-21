from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creative import Creative


@dataclass
class BrandRestrictionIssueCreative:
    """
    Creative with Brand Restriction Issues
    """
    creative: Optional[Creative]
    isPending: bool

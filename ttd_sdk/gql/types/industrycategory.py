from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .categorymapping import CategoryMapping
    from .categorytaxonomy import CategoryTaxonomy


@dataclass
class IndustryCategory:
    """
    None
    """
    id: str
    isDefault: bool
    isSensitive: bool
    mappings: List[Optional[CategoryMapping]]
    name: str
    parentCategoryId: str
    taxonomy: Optional[CategoryTaxonomy]

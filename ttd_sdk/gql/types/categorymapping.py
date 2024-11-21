from dataclasses import dataclass

@dataclass
class CategoryMapping:
    """
    The mappings between the industry category taxonomies (IAB 1.0 and IAB 2.2)
    """
    categoryId: int
    externalId: str
    taxonomyId: int

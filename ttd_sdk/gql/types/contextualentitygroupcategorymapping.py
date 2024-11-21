from dataclasses import dataclass

@dataclass
class ContextualEntityGroupCategoryMapping:
    """
    Represents contextual entity group category mapping in the contextual marketplace.
    """
    categoryId: str
    contextualEntityGroupId: str
    ordering: int

from dataclasses import dataclass

@dataclass
class CategoryProvider:
    """
    Represents a provider for category names/taxonomy, such as Facebook/Google/Shopify (third-party) or a custom one (first-party).
    """
    id: str
    isThirdParty: bool
    providerName: str

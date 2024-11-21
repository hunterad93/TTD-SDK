from dataclasses import dataclass

@dataclass
class AdPolicyViolationExemption:
    """
    None
    """
    exemptedAt: Any
    exemptedBy: str
    reason: str

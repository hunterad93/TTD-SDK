from dataclasses import dataclass

@dataclass
class BudgetEstimationResponse:
    """
    The response for pg adGroup budget estimation query.
    """
    estimatedBudget: Any

from dataclasses import dataclass

@dataclass
class SubmitCreativeForApprovalOutput:
    """
    Creative approval data for optional SSPs.
    """
    submitToStroerForReview: bool
    submitToVioohForReview: bool
    vioohSelectedPublisher: str

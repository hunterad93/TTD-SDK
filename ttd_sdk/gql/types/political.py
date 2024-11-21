from dataclasses import dataclass
from typing import List

@dataclass
class Political:
    """
    None
    """
    candidateCount: int
    categoryIds: List[str]
    isBallotMeasure: bool
    isCandidateElection: bool

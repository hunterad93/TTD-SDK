from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .affectedentitiesconnection import AffectedEntitiesConnection
    from .jobstatus import JobStatus


@dataclass
class JobProgress:
    """
    None
    """
    affectedEntities: Optional[AffectedEntitiesConnection]
    id: str
    jobStatus: Optional[JobStatus]
    resultUrl: str
    validationErrors: str

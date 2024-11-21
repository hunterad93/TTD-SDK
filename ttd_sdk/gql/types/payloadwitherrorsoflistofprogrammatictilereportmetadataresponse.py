from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .programmatictilereportmetadataresponse import ProgrammaticTileReportMetadataResponse
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfListOfProgrammaticTileReportMetadataResponse:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: List[Optional[ProgrammaticTileReportMetadataResponse]]
    userErrors: List[Optional[UserError]]

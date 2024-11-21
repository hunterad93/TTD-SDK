from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativechannel import CreativeChannel
    from .crosschannelverificationissue import CrossChannelVerificationIssue


@dataclass
class CrossChannelVerification:
    """
    None
    """
    channel: Optional[CreativeChannel]
    isPending: bool
    issues: List[Optional[CrossChannelVerificationIssue]]

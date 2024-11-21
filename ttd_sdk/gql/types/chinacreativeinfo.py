from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .miniprogram import MiniProgram


@dataclass
class ChinaCreativeInfo:
    """
    None
    """
    chinaThirdPartyClickTrackingUrl: str
    isWechatMomentOnlyForTencent: bool
    miniProgram: Optional[MiniProgram]
    nativeLandingPageId: str

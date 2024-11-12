from typing import Dict, Optional, List
from pydantic import BaseModel

class ExactMatchMapping(BaseModel):
    Url: Optional[str] = None

class WildcardMatchMapping(BaseModel):
    Pattern: Optional[str] = None

class UniversalPixelMappings(BaseModel):
    ExactMatchMappings: Optional[List[ExactMatchMapping]] = None
    WildcardMatchMappings: Optional[List[WildcardMatchMapping]] = None

class UniversalPixel(BaseModel):
    UniversalPixelId: Optional[str] = None
    UniversalPixelName: Optional[str] = None
    AdvertiserId: Optional[str] = None
    Description: Optional[str] = None
    UniversalPixelMappings: Optional[UniversalPixelMappings] = None

class UniversalPixelCode(BaseModel):
    UniversalPixelId: Optional[str] = None
    UniversalPixelName: Optional[str] = None
    PixelCode: Optional[str] = None
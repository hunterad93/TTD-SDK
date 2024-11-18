import json
from typing import Dict, Any

class ApiObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                value = ApiObject(**value)
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                value = [ApiObject(**item) for item in value]
            setattr(self, key, value)
    
    def to_dict(self) -> dict:
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, ApiObject):
                value = value.to_dict()
            elif isinstance(value, list):
                value = [item.to_dict() if isinstance(item, ApiObject) else item for item in value]
            result[key] = value
        return result
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict())
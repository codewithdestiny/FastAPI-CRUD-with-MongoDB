from pydantic import BaseModel, Field
from typing import List

class TodoBase(BaseModel):
    title : str = Field(...)
    body : List[str] = Field(...)
    

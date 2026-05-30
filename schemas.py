from pydantic import BaseModel
from typing import Optional

class blogy(BaseModel):
    title:str
    providers:str
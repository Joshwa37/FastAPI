from typing import Optional
from pydantic import BaseModel, ConfigDict

class blogy(BaseModel):
    title:str
    providers:str

class mode(BaseModel):
    title:str                       
    model_config = ConfigDict(from_attributes=True)

class userl(BaseModel):
    name:str
    email:str
    password:str

class usermode(BaseModel):
    name:str
    email:str
    model_config = ConfigDict(from_attributes=True)


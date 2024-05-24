from pydantic import BaseModel
from typing import Optional

class RawDataBase(BaseModel):
    source: str
    data: str

class RawDataCreate(RawDataBase):
    pass

class RawData(RawDataBase):
    id: int

    class Config:
        orm_mode = True

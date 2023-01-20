from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from pydantic import Field, BaseModel
from esgscoringlewagon.api.schemas.articleSchema import article

class companyBase(BaseModel):
    name : str 
    description : Optional[str] = None
    class Config:
        orm_mode = True



class companyCreate(companyBase):
    pass

class companyUpdate(BaseModel):
    name : Optional[str] 
    description : Optional[str]
    class Config:
        orm_mode = True


class company(companyBase):
    id : int
    articles : article = None
    class Config:
        orm_mode = True
    
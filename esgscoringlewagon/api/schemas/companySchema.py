from pydantic import BaseModel, Field
from typing import Union, List
from esgscoringlewagon.api.schemas.articleSchema import ArticleDetail
class CompanyBase(BaseModel):
    name : str = Field(..., min_length=1)
    description : Union[str, None] = None
    class Config:
        orm_mode = True

class CompanyName(BaseModel):
    name : str = Field(..., min_length=1)
    class Config:
        orm_mode = True


class CompanyCreate(CompanyBase):
    pass
    class Config:
        orm_mode = True



class Company(CompanyBase):
    id: int
    articles: List[ArticleDetail] = []
    class Config:
        orm_mode = True
    
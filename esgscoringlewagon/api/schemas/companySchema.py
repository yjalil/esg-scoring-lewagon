from pydantic import BaseModel
from typing import Union, List
from esgscoringlewagon.api.schemas.articleSchema import Article
class CompanyBase(BaseModel):
    name : str 
    description : Union[str, None] = None
    class Config:
        orm_mode = True



class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    articles: List[Article] = []
    class Config:
        orm_mode = True
    
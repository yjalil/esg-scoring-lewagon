from pydantic import BaseModel
import datetime
from esgscoringlewagon.api.schemas import companySchema
from typing import List, Optional

class articleBase(BaseModel):
    company_name : str
    date : datetime.date
    uploaded_at : datetime.date
    title : str 
    body : str 
    sourceURL : str
    topic_category : str
    esg_score : float
    scored_at :  datetime.date
    exclude_count : int
    class Config:
        orm_mode = True

class articleUpdate(BaseModel):
    date : Optional[datetime.date]
    uploaded_at : Optional[datetime.date]
    title : Optional[str] 
    body : Optional[str]
    sourceURL : Optional[str]
    topic_category : Optional[str]
    esg_score : Optional[float]
    scored_at :  Optional[datetime.date]
    exclude_count : Optional[int]
    class Config:
        orm_mode = True


class articleCreate(articleBase):
    pass
    class Config:
        orm_mode = True

class article(articleBase):
    id : int
    class Config:
        orm_mode = True
    
    
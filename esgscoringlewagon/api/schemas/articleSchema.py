from pydantic import BaseModel
from datetime import datetime

class ArticleBase(BaseModel):
    
    date : datetime
    title : str
    uploaded_at : datetime
    body : str 
    sourceURL : str
    topic_category : str
    esg_score : float
    scored_at :  datetime
    exclude_count : int
    class Config:
        orm_mode = True



class ArticleCreate(ArticleBase):
    pass
    class Config:
        orm_mode = True

class Article(ArticleBase):
    id : int
    owner_id : int
    class Config:
        orm_mode = True
    
    
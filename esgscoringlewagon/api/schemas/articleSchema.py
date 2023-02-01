from pydantic import BaseModel, Field
from datetime import datetime

class ArticleBase(BaseModel):
    date : datetime
    title : str = Field(..., min_length=3)
    uploaded_at : datetime
    body : str = Field(..., min_length=10)
    sourceURL : str = Field(..., min_length=3)
    topic_category : str = Field(..., min_length=3)
    esg_score : float
    scored_at :  datetime
    exclude_count : int
    class Config:
        orm_mode = True

class ArticlePredictIn(BaseModel):
    body : str = Field(..., min_length=10)
    class Config:
        orm_mode = True

class ArticlePredictOut(BaseModel):
    topic_category : str = Field(..., min_length=3)
    esg_score : float
    class Config:
        orm_mode = True

class ArticleDetail(BaseModel):
    date : datetime
    title : str = Field(..., min_length=3)
    body : str = Field(..., min_length=10)
    sourceURL : str = Field(..., min_length=3)
    topic_category : str = Field(..., min_length=3)
    esg_score : float
    class Config:
        orm_mode = True

class ArticleGraph(BaseModel):
    date : datetime
    topic_category : str = Field(..., min_length=3)
    esg_score : float
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
    
    
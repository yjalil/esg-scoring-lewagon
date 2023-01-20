from sqlalchemy import DateTime, Column, Float,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from esgscoringlewagon.api.db.db_setup import Base
from typing import TYPE_CHECKING
from esgscoringlewagon.api.models import companyModel

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    uploaded_at = Column(DateTime)
    title = Column(String)
    body = Column(String)
    sourceURL = Column(String)
    topic_category = Column(String)
    esg_score = Column(Float)
    scored_at = Column(DateTime)
    exclude_count = Column(Integer)
    
    company_name = Column(String, ForeignKey("companies.name"))
    company = relationship("Company", back_populates="articles",uselist=True)
    
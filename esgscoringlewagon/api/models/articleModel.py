from sqlalchemy import DateTime, Column, Float,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from esgscoringlewagon.api.db.db_setup import Base
from esgscoringlewagon.api.models.companyModel import Company
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime,nullable=False)
    uploaded_at = Column(TIMESTAMP(timezone=True),nullable=False)
    title = Column(String)
    body = Column(String)
    sourceURL = Column(String)
    topic_category = Column(String)
    esg_score = Column(Float)
    scored_at = Column(DateTime)
    exclude_count = Column(Integer)
    
    owner_id = Column(Integer, ForeignKey("companies.id"))
    owner = relationship("Company",back_populates="articles")
    
from sqlalchemy import DateTime, Column, Float,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from esgscoringlewagon.api.db.db_setup import Base
from esgscoringlewagon.api.models.companyModel import Company
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    date = Column(String,nullable=False)
    uploaded_at = Column(String,nullable=False)
    title = Column(String,unique=True,nullable=False)
    body = Column(String,unique=True,nullable=False)
    sourceURL = Column(String)
    topic_category = Column(String)
    esg_score = Column(Float)
    scored_at = Column(String)
    exclude_count = Column(Integer)
    
    owner_id = Column(Integer, ForeignKey("companies.id",ondelete='CASCADE'))
    owner = relationship("Company",back_populates="articles")
    
    
    
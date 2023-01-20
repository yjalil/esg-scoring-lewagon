from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from esgscoringlewagon.api.db.db_setup import Base
# from esgscoringlewagon.api.models.articleModel import Article


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, index=True)
    name = Column(String, index=True,unique=True, primary_key=True)
    description = Column(String)
    
    articles = relationship("Article",back_populates="company",uselist=False)
    

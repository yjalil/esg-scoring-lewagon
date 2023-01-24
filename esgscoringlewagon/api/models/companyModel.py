from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from esgscoringlewagon.api.db.db_setup import Base
# from esgscoringlewagon.api.models.articleModel import Article


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False,unique=True)
    description = Column(String)
    
    articles = relationship("Article", back_populates="owner",cascade="all,delete-orphan")

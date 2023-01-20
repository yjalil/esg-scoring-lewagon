from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException

from esgscoringlewagon.api.models import articleModel
from esgscoringlewagon.api.schemas import articleSchema
from esgscoringlewagon.api.crud.companyCRUD import get_company_by_name

def create_company_article(db: Session, company_name :str, article: articleSchema.articleCreate):
    isCompany = get_company_by_name(db, company_name)
    if isCompany is None:
        raise HTTPException(status_code=404, detail="This company doesn't exit")
    db_article = articleModel.Article(company_name = article.company_name,
                                      date = article.date,
                                      uploaded_at = datetime.now(),
                                      title = article.title,
                                      body = article.body,
                                      sourceURL = article.sourceURL,
                                      topic_category = article.topic_category,
                                      esg_score = article.esg_score,
                                      scored_at = article.scored_at,
                                      exclude_count = 0)
                                                
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return "Article added to db successfully"


def get_article_by_company_name(db : Session, company_name: str):
    return db.query(articleModel.Article).filter(articleModel.Article.company_name == company_name).all()

def get_article_by_id(db : Session, id: str):
    return db.query(articleModel.Article).filter(articleModel.Article.id == id).first()

def update_article(db:Session, id:int, article:articleSchema.article):
    db_article = db.query(articleModel.Article).filter(articleModel.Article.id == id).first()
    db_article.date = article.date
    db_article.uploaded_at = datetime.now()
    db_article.title = article.title
    db_article.body = article.body,
    db_article.sourceURL = article.sourceURL,
    db_article.topic_category = article.topic_category,
    db_article.esg_score = article.esg_score,
    db_article.scored_at = article.scored_at,
    db_article.exclude_count = 0
    db.commit()
    db.refresh(db_article)
    


def delete_article(id : int, db : Session):
    db_article = db.query(articleModel.article).filter(articleModel.article.id == id).first()
    db.delete(db_article)
    db.commit()

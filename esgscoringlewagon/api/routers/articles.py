from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import ValidationError
from typing import List
from sqlalchemy.exc import IntegrityError
from esgscoringlewagon.api.models import articleModel, companyModel
from esgscoringlewagon.api.schemas import articleSchema, companySchema
from esgscoringlewagon.api.db.db_setup import get_db, Session
router = APIRouter()



@router.get("/articles/", response_model=List[articleSchema.Article]) 
def get_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_articles =db.query(articleModel.Article).all()
    return db_articles

@router.get("/articles/byCompany/{company_name}", response_model=List[articleSchema.Article]) 
def get_articles_by_company(company_name: str,db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    try :
        db_company = db.query(companyModel.Company).filter(companyModel.Company.name == company_name).first()
        db_articles =db_company.articles
        return db_articles
    except :
        raise HTTPException(status_code=404,
                            detail=f"Company {company_name} does not exist")
    
@router.get("/articles/byCompany/{company_name}/Period/{start_date}/{end_date}", response_model=List[articleSchema.ArticleGraph]) 
def get_articles_by_company_period(company_name: str, start_date:str, end_date:str,db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    
        db_company = db.query(companyModel.Company).filter(companyModel.Company.name == company_name).first()
        db_articles =db_company.articles
        
        return [article for article in db_articles if article.date >= datetime.strptime(start_date, '%Y-%m-%d') and article.date <= datetime.strptime(end_date, '%Y-%m-%d')]
    # except :
    #     raise HTTPException(status_code=404,
    #                         detail=f"Company {company_name} does not exist")


@router.get("/article/byId/{article_id}",response_model=articleSchema.Article)
def get_article_by_id(article_id : int, db : Session=Depends(get_db)):
    db_article = db.query(articleModel.Article).filter(articleModel.Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404,
                            detail=f"The article does not exist")
    return db_article

@router.get("/articles/byDate/{articles_date}",response_model=List[articleSchema.Article])
def get_article_by_date(articles_date : datetime, db : Session=Depends(get_db)):
    db_articles = db.query(articleModel.Article).filter(articleModel.Article.date == articles_date).all()
    if not db_articles:
        raise HTTPException(status_code=404,
                            detail=f"No article found for{articles_date}")
    return db_articles

@router.post("/article/add/{company_name}",status_code =201, response_model = articleSchema.Article)
def create_article(article: articleSchema.ArticleCreate, company_name: str, db: Session = Depends(get_db)):
    try : 
        db_company = db.query(companyModel.Company).filter(companyModel.Company.name == company_name).first()
        if not  db_company:
            raise HTTPException(status_code=404,
                                detail=f"No company found with the name : {company_name}")
        
        db_article = articleModel.Article(**article.dict(), owner_id=db_company.id)
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,
                            detail=f"Article title or body fields already exist")


@router.delete("/article/delete/{article_id}", status_code = 204)
def delete_article(article_id : int,db : Session=Depends(get_db)):
    db_article_deleteQuery = db.query(articleModel.Article).filter(articleModel.Article.id == article_id)
    db_article = db_article_deleteQuery.first()
    if db_article is None:
        raise HTTPException(status_code=404,
                            detail=f"The article does not exist")
    db_article_deleteQuery.delete()
    db.commit()
    
    return Response(status_code = 204)

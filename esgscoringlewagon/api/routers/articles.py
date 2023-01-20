from esgscoringlewagon.api.schemas import companySchema
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from esgscoringlewagon.api.schemas import articleSchema
from esgscoringlewagon.api.crud import articleCRUD
from esgscoringlewagon.api.db.db_setup import get_db, Session
router = APIRouter()



@router.post("/companies/{company_name}/article",response_model=articleSchema.articleCreate)
def create_company_article(company_name:str, article: articleSchema.articleCreate, db: Session = Depends(get_db)):
    return articleCRUD.create_company_article(db, company_name, article) 

@router.get("/companies/{company_name}/article",response_model=List[articleSchema.article])
def read_company_article(company_name : str, db : Session=Depends(get_db)):
    db_article = articleCRUD.get_article_by_company_name(db,company_name)
    if db_article is None:
        raise HTTPException(status_company_name=404, detail="Cet écheancier n'existe pas")
    return db_article

@router.put("/companies/{company_name}/article")
def change_company_article(company_name : str, article : articleSchema.article, db : Session=Depends(get_db)):
    db_article = articleCRUD.get_article_by_company_company_name(db,company_name)
    if db_article:
        return articleCRUD.update_article(db, company_name, article)
    else:
        raise HTTPException(status_company_name=404, detail="This article doesn't exist")

@router.delete("/companies/{company_name}/article",response_model=articleSchema.article)
def destroy_company_article(company_name : str,db : Session=Depends(get_db)):
    db_article = articleCRUD.get_article_by_company_company_name(db,company_name)
    if db_article:
        return articleCRUD.delete_article(company_name, db)
    if db_article is None:
        raise HTTPException(status_company_name=404, detail="This article doesn't exist")
    



    
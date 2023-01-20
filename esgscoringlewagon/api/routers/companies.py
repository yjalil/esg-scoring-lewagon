from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from esgscoringlewagon.api.schemas import companySchema
from esgscoringlewagon.api.crud import companyCRUD
from esgscoringlewagon.api.db.db_setup import get_db, Session
from typing import List

router = APIRouter()



@router.get("/companies/", response_model=List[companySchema.companyBase]) #
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = companyCRUD.get_companies(db, skip=skip, limit=limit)
    return companies

@router.get("/companies/{company_name}",response_model=companySchema.companyBase)
def read_company(company_name : str, db : Session=Depends(get_db)):
    db_company = companyCRUD.get_company_by_name(db,company_name)
    if db_company is None:
        raise HTTPException(status_code=404, detail="This company doesn't exist")
    return db_company

@router.post("/companies/")
def create_company(company: companySchema.companyCreate, db: Session = Depends(get_db)):
    db_company = companyCRUD.get_company_by_name(db,company.name)
    if db_company is None :
        return companyCRUD.create_company(db,company)
    if db_company :
        raise HTTPException(status_code=409, detail=" This company already exists", )
    return JSONResponse(status_code=409, content="409 Conflit : company already exists ") 


@router.patch("/companies/{company_name}")
def change_company(company_name : str, company : companySchema.companyUpdate, db : Session=Depends(get_db)):
    db_company = companyCRUD.get_company_by_name(db,company_name)
    if db_company :
        return companyCRUD.update_company(db, db_company, company)
    if db_company is None :
        raise HTTPException(status_code=404, detail=" This company doesn't exist", )
    return JSONResponse(status_code=404, content="404 not found : company doesn't exist ")
    
@router.delete("/companies/{company_name}")
def destroy_company(company_name : str,db : Session=Depends(get_db)):
    db_company = companyCRUD.get_company_by_name(db, company_name)
    if db_company:
        return companyCRUD.delete_company(db,company_name)
    if db_company is None:
        raise HTTPException(status_code=404, detail="This company doesn't exist")

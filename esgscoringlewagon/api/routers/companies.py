from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from esgscoringlewagon.api.schemas import companySchema
from esgscoringlewagon.api.models import companyModel
from esgscoringlewagon.api.db.db_setup import get_db, Session
from typing import List

router = APIRouter()

@router.get("/companies/", response_model=List[companySchema.CompanyName]) #
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_companies =db.query(companyModel.Company).all()
    return db_companies


@router.get("/companies/{company_name}",response_model=companySchema.Company)
def get_company_by_name(company_name : str, db : Session=Depends(get_db)):
    db_company = db.query(companyModel.Company).filter(companyModel.Company.name == company_name).first()
    if not db_company:
        raise HTTPException(status_code=404,
                            detail=f"The company named: {company_name} does not exist")
    return db_company

@router.post("/company/add/",status_code =201, response_model = companySchema.Company)
def create_company(company: companySchema.CompanyCreate, db: Session = Depends(get_db)):
    new_company  = companyModel.Company(**company.dict())
    try:
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return(new_company)
    except:
        raise HTTPException(status_code=409, detail=f"{new_company.name} already exists. Company names must be unique")



@router.put("/company/update/{company_name}",response_model = companySchema.Company)
def update_company(company_name : str, updated_company: companySchema.CompanyCreate,db : Session=Depends(get_db)):
    db_company_updateQuery = db.query(companyModel.Company).filter(companyModel.Company.name == company_name)
    db_company = db_company_updateQuery.first()
    if db_company is None:
         raise HTTPException(status_code=404,
                            detail=f"The company named: {company_name} does not exist")
    db_company_updateQuery.update(updated_company.dict())
    db.commit()
    return db.query(companyModel.Company).filter(companyModel.Company.name == updated_company.name).first()
        

@router.delete("/company/delete/{company_name}", status_code = 204)
def delete_company(company_name : str,db : Session=Depends(get_db)):
    db_company_deleteQuery = db.query(companyModel.Company).filter(companyModel.Company.name == company_name)
    db_company = db_company_deleteQuery.first()
    if db_company is None:
        raise HTTPException(status_code=404,
                            detail=f"The company named: {company_name} does not exist")
    db_company_deleteQuery.delete()
    db.commit()
    
    return Response(status_code = 204)

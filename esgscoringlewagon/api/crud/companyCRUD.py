from sqlalchemy.orm import Session

from esgscoringlewagon.api.models import companyModel
from esgscoringlewagon.api.schemas import companySchema

def create_company(db: Session, company: companySchema.companyCreate):
    db_company = companyModel.Company(name= company.name,
                                description= company.description)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return "company added to db successfully"


def get_company_by_name(db : Session, name: str):
    return db.query(companyModel.Company).filter(companyModel.Company.name == name).first()

def get_company_by_id(db : Session, company_id: int):
    return db.query(companyModel.Company).filter(companyModel.Company.id == company_id).first()


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(companyModel.Company).offset(skip).limit(limit).all()

def update_company(db : Session, db_company : companyModel.Company, company: companySchema.companyUpdate):
    if company.name:
        db_company.name = company.name
    if company.description:   
        db_company.description= company.description
    db.commit()
    db.refresh(db_company)
    return db_company

def delete_company(db : Session, company_name : str):
    db_company = db.query(companyModel.Company).filter(companyModel.Company.name == company_name).first()
    db.delete(db_company)
    db.commit()
    return "company deleted from db successfully"



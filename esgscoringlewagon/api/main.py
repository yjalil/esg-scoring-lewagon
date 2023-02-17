from esgscoringlewagon.api.routers import articles, companies
from fastapi import FastAPI
from esgscoringlewagon.api.db.db_setup import Base, SessionLocal, engine
from esgscoringlewagon.api.routers import articles, companies, ml
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware


origin = "http://localhost:3000"
class MyHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = '*'
        response.headers["Access-Control-Allow-Headers"] = 'Content-Type, Authorization'
        response.headers["Access-Control-Allow-Credentials"] = "True"
        return response

 

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()
app.add_middleware(
    MyHeadersMiddleware    
)

# app.include_router(files.router)

@app.get('/')
def root():
    return {'message':'API is online'}
app.include_router(companies.router)
app.include_router(articles.router)
app.include_router(ml.router)



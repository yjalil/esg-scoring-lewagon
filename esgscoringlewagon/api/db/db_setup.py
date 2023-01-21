from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from esgscoringlewagon.api.config import AppConfig


config = AppConfig()

cnn_str = config.db_extension+':///./'+config.db_name+'.'+config.db_extension

print(cnn_str)

engine = create_engine(cnn_str)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

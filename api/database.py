from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker , Session

SQLALCHEMY_DATABASE_URL ="mysql://root:@localhost:3306/real_estate"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

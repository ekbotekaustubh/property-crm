from fastapi import FastAPI, Depends 
from sqlalchemy.orm import sessionmaker , Session
from dtos import user, user_login
from pwdlib import PasswordHash
from sqlalchemy import Enum
from models import Base, User
from database import engine, get_db




app =FastAPI() 

   
@app.get("/")
def home():
    return("Welcome to Fast Api Serise ...")

password_hash = PasswordHash.recommended()
def get_password_hash(password):
    return password_hash.hash(password)


@app.post("/creat_user")
def create_user(body:user, db: Session = Depends(get_db)):
    is_user = db.query(User).filter(User.email == body.email ).first()
    if is_user:
        return {"msg":"Gmail already exites..."}
    hash_password = get_password_hash(body.password)
    new_user = User( first_name = body.first_name, last_name = body.last_name,email=body.email,password = hash_password,phone = body.phone)
    db.add(new_user)
    db.commit()

    print(body)
    return {"msg":"user created sussfully..."}

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)



@app.get("/user_login")
def usre_login(body: user_login, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email ).first()
    if not user:
        return {"msg":"Invalied gmail..."}
    if not verify_password(body.password, user.password):
        return {"masg":"Invalied Password..."}

     
    if user and verify_password(body.password, user.password) :
        return {"msg":"login sussesfull..."} 
    else:
        return{"msg":"Login Unsussfull..."}
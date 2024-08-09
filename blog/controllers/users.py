from fastapi import  HTTPException, Depends
from datetime import datetime, timedelta, timezone
from ..database import db_dependency
from ..schema import CreateUser, LoginUser
from .. import models 
from ..bcrypt import Hash
from ..jwtToken import create_access_token
from ..schema import Token, TokenData
from typing import Annotated, List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def create_user(db :db_dependency, request :CreateUser ) :
    user = models.User(username=request.username, email =request.email, password =Hash.get_password_hash(request.password) )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
  
def login_user(db :db_dependency, request :Annotated[OAuth2PasswordRequestForm, Depends()] ) :
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if user is None :
      raise HTTPException(status_code=401, detail="No user found")
    hashPass = Hash.verify_password(request.password, user.password)
    if hashPass is False :
      raise HTTPException(status_code=401, detail="Invalid password")
    
    
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return Token(access_token=access_token, token_type="bearer")

def single_user(db :db_dependency , id :int) :
     user = db.query(models.User).filter(models.User.id==id).first()     
     if user is None :
       raise HTTPException(status_code=404, detail="No User Found")
     return user
from fastapi import  HTTPException
from ..database import db_dependency
from ..schema import CreateUser, ShowUser
from .. import models 
from ..bcrypt import Hash

def create_user(db :db_dependency, request :CreateUser ) :
    user = models.User(username=request.username, email =request.email, password =Hash.get_password_hash(request.password) )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def single_user(db :db_dependency , id :int) :
     user = db.query(models.User).filter(models.User.id==id).first()     
     if user is None :
       raise HTTPException(status_code=404, detail="No User Found")
     return user
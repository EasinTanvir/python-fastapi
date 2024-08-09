from fastapi import APIRouter, status, Depends
from ..schema import CreateUser, ShowUser, LoginUser
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..database import db_dependency
from ..controllers import users
from typing import Annotated, List

router = APIRouter(
    prefix='/user',
     tags=['user routes']
)

@router.post("/register", response_model=ShowUser, )
def create_user(db : db_dependency, request : CreateUser) :
   return users.create_user(db, request)   

@router.post("/login")
def login_user(db : db_dependency, request : Annotated[OAuth2PasswordRequestForm, Depends()]) :
   return users.login_user(db, request)   

@router.get("/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK, )   
def get_user(db : db_dependency, id:int) :
       return users.single_user(db, id)
  


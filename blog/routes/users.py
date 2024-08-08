from fastapi import APIRouter, status
from ..schema import CreateUser, ShowUser
from ..database import db_dependency
from ..controllers import users


router = APIRouter(
    prefix='/user',
     tags=['user routes']
)

@router.post("/", response_model=ShowUser, )
def create_user(db : db_dependency, request : CreateUser) :
   return users.create_user(db, request)   

@router.get("/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK, )   
def get_user(db : db_dependency, id:int) :
       return users.single_user(db, id)
  


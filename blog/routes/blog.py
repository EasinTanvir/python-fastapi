from fastapi import APIRouter,   Response, status, Depends
from typing import  List
from ..schema import CreateBlog, CreateSeconBlog, ShowBlog, CreateUser
from ..database import db_dependency
from ..controllers import blog
from ..protectRoute import get_current_user

router = APIRouter(
   prefix='/blog',
   tags=['blog routes']
)

@router.get("/", response_model=List[ShowBlog])
def get_all_blogs(db:db_dependency, get_current_user:CreateUser = Depends(get_current_user) ) :
   return blog.all_posts_contrl(db)

@router.get("/{id}", response_model=ShowBlog)
def get_blog(id:int, db:db_dependency, get_current_user:CreateUser = Depends(get_current_user) ) :
   return blog.get_single_post(db, id)
  
@router.put("/{id}")
def update_blog(id: int, request: CreateSeconBlog, db:db_dependency):
   return blog.update_post(db,id,request)   

@router.delete("/{id}")
def delete_blog(id:int, db:db_dependency ,response : Response) :
   return blog.delete_post(id,db,response) 
      
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: CreateBlog, db : db_dependency) :   
   return blog.create_post(request,db)

from fastapi import  HTTPException, status, Response
from ..schema import CreateBlog, CreateSeconBlog, ShowBlog
from ..database import db_dependency
from .. import models  
from .. import protectRoute  

 
def all_posts_contrl(db : db_dependency) :
   return db.query(models.Blog).all()


def get_single_post(db : db_dependency, id:int) :
    
   single= db.query(models.Blog).filter(models.Blog.id == id).first()
   if single is None :
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid BlogId")
   else :
     return single    
 
 
def update_post(db:db_dependency, id:int, request:CreateSeconBlog) :
     
     blog_to_update = db.query(models.Blog).filter(models.Blog.id == id).first()
    
     if not blog_to_update:
        raise HTTPException(status_code=404, detail="Blog not found")

     if request.title is not None:
        blog_to_update.title = request.title
     if request.desc is not None:
        blog_to_update.desc = request.desc
    
     db.commit()
     return {"message": "Blog updated successfully"}
 
 
def delete_post(id, db, response :Response) :
    
     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
     db.commit()
     response.status_code =201    
     
     return {"message":"deleted"}
 
def create_post(request: CreateBlog, db : db_dependency) :
    
   new_blog = models.Blog(title =request.title, desc = request.desc, creator_id = request.creator_id)   
   db.add(new_blog)
   db.commit()
   db.refresh(new_blog)   
   return new_blog
 
 

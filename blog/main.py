from fastapi import FastAPI, Depends, status, HTTPException, Response
from typing import Annotated, List
from .import  models
from .schema import CreateBlog, CreateSeconBlog, ShowBlog
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]



@app.get("/blog", response_model=List[ShowBlog])
def get_all_blogs(db:db_dependency) :
   return db.query(models.Blog).all()

@app.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id:int, db:db_dependency,) :
   single= db.query(models.Blog).filter(models.Blog.id == id).first()
   if single is None :
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid BlogId")
   else :
     return single
  
@app.put("/blog/{id}")
def update_blog(id: int, request: CreateSeconBlog, db:db_dependency):
    blog_to_update = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog_to_update:
        raise HTTPException(status_code=404, detail="Blog not found")

    if request.title is not None:
        blog_to_update.title = request.title
    if request.desc is not None:
        blog_to_update.desc = request.desc
    
    db.commit()
    return {"message": "Blog updated successfully"}
        


@app.delete("/blog/{id}")
def delete_blog(id:int, db:db_dependency ,response : Response) :
 
     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
     db.commit()
     response.status_code =201    
     
     return {"message":"deleted"}
   
      


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: CreateBlog, db : db_dependency) :   
   new_blog = models.Blog(title =request.title, desc = request.desc)   
   db.add(new_blog)
   db.commit()
   db.refresh(new_blog)   
   return new_blog







   
   

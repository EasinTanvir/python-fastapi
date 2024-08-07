from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class CreateBlog(BaseModel) :
  title :str
  desc :str
  publish : Optional[bool] = False




# '@' path operation decorator, 'get' is the operation and '/' is the path
@app.get("/")
# path operation function
def test() :
    return {"data": "homepage" }


# query
@app.get("/blogs")

def all_blogs(name :str='', publish : bool = False, isvalid :Optional[str] = None) :     

    
    
    if publish :
      return {"data": f"{name} published Blog query"}
    else :
      return {"data": f"{name} Blog query"}


@app.get("/blog/private")

def private_data() :
    return {"data" :"all private data"}


@app.get("/blog/{id}")

def single_blex(id : int) :
    return {"blogId" :id}


@app.post("/blog")
def create_blog(blog : CreateBlog) :   
   return blog


from pydantic import BaseModel
from typing import Optional, List

class CreateBlog(BaseModel) :
    title : str
    desc : str
    creator_id : int
    
class CreateUser(BaseModel) :
     username : str
     email : str
     password : str
     

     
class ShowUser(BaseModel) :
     username : str
     email : str
     blogs : List[CreateBlog]
     

     
class ShowBlog(BaseModel) :
   title : str
   creator_id :int
   creator :ShowUser



   
    
class CreateSeconBlog(BaseModel) :
    title : Optional[str] = None
    desc : Optional[str] = None
    

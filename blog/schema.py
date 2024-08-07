from pydantic import BaseModel
from typing import Optional

class CreateBlog(BaseModel) :
    title : str
    desc : str
    
class ShowBlog(BaseModel) :
   title : str
    
class CreateSeconBlog(BaseModel) :
    title : Optional[str] = None
    desc : Optional[str] = None

from fastapi import FastAPI
from .import  models
from .database import engine
from .routes import blog, users

        


app = FastAPI()

app.include_router(blog.router)
app.include_router(users.router)


models.Base.metadata.create_all(bind=engine)




        
  
   






   
   

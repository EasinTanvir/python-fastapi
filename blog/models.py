from sqlalchemy import Column, Integer, String, Boolean , ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    desc = Column(String(100))
    creator_id = Column(Integer, ForeignKey("clients.id"))
    creator = relationship("User", back_populates="blogs")

class User(Base) :
    __tablename__ ='clients'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100))
    password = Column(String(255))
    isAdmin = Column(Boolean, default=False)
    
    blogs = relationship("Blog", back_populates="creator")
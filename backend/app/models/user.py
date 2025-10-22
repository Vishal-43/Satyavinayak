from sqlalchemy import Column,Integer,String, Boolean, DateTime
from .base import base

class user(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    email = Column(String, unique=True, index=True,nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String,default="member")
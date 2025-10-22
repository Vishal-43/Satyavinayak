from sqlalchemy import Column,Integer,String, Boolean, DateTime
from .base import base

class member(base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index = True,autoincrement=True)
    user_id = Column(Integer, nullable=False, foreign_key="users.id")
    room_no = Column(String, nullable = False)
    wing = Column(String,nullable=False)
    name = Column(String, nullable=False)
    Phone=Column(String, nullable=False)
    family_members=Column(Integer, nullable=False)
    ownbership_type=Column(String, nullable=False)
    move_in_date=Column(DateTime,nullable=False)
    
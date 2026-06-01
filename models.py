from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class blog(Base):
    __tablename__='blog'

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    providers=Column(String)

class user(Base):
    __tablename__='user'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)


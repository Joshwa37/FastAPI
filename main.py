from fastapi import FastAPI,Depends,HTTPException,status
from typing import Optional,List
from models import blog
from database import engine,Base
from sqlalchemy.orm import Session
from database import SessionLocal,get_db
import models
from schemas import blogy,mode,userl,usermode
from pydantic import BaseModel
  
app=FastAPI()


models.Base.metadata.create_all(engine) 





@app.get('/')
def home():
    return {'data':{'name':"jos"}}


@app.get('/about')
@app.get('/about/{id}')
def about(id=10):
    return {'data':f"{id}it is a about page"}

@app.post('/blog',status_code=201,tags=['blogs'])
def bloge(req:blogy ,db:Session=Depends(get_db)):
    new_blog=models.blog(title=req.title , providers=req.providers)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog',response_model=List[mode],tags=['blogs'])
def getblog(db:Session=Depends(get_db)):
    blogs=db.query(models.blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200,tags=['blogs'])
def getspec(id,db:Session=Depends(get_db)):
    blogs=db.query(models.blog).filter(models.blog.id==id).first()
    if(not blogs):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Not have the {id} details')
    return blogs

@app.delete('/blog/{id}',tags=['blogs'])
def delblog(id,db:Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if(not blog.first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Not have the {id} details')
    else:
        blog.delete(synchronize_session=False)
    db.commit()
    return f'delete has happened'

@app.put('/blog/{id}',tags=['blogs'])
def updblog(id,req:blogy,db:Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if(not blog.first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Not have the {id} details')
    else:
        req=req.model_dump()
        blog.update(req,synchronize_session=False)
    db.commit()
    return 'update'

@app.post('/user',tags=['user'],response_model=usermode)
def users(req:userl,db:Session=Depends(get_db)):
    new_user=models.user(name=req.name,email=req.email,password=req.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',tags=['user'],response_model=List[usermode])
def userdata(id,db:Session=Depends(get_db)):
    usersd=db.query(models.user).filter(models.user.id==id).first()
    if(not usersd):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Not have the {id} details')
    return usersd



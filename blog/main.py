from typing import List
from fastapi import FastAPI, Depends, status,Response, HTTPException
from passlib.utils.decor import deprecated_function
from sqlalchemy.sql.functions import mode
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .hashing import Hash
from .routers import blogs, users, authentication
 
import blog
app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()










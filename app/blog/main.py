
from fastapi import FastAPI, Depends, status,Response, HTTPException
from blog import schemas, models
from blog.database import engine, get_db
from blog.routers import blogs, users, authentication
 
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










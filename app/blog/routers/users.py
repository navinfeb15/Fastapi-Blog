from fastapi import APIRouter, Depends
from blog import schemas

from blog.database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(prefix="/user", tags=["User"])

@router.post('/', response_model= schemas.ShowUser)
def create_user(request: schemas.User, db: Session= Depends(get_db)):
    return user.create_user(request, db)



@router.get('//{id}', response_model=schemas.ShowUserwb)
def get_user(id:int, db: Session= Depends(get_db)):

    return user.view_user(id,db)
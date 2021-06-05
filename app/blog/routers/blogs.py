from fastapi import APIRouter, status, Depends
from typing import List
from blog import schemas, database
from sqlalchemy.orm import Session
from blog import oauth2
from ..repository import blog


router = APIRouter(prefix="/blog",tags=["Blog"])



@router.get('/',response_model=List[schemas.ShowBlog])
def get_all_blog(db:Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/',status_code= status.HTTP_201_CREATED )
def create(request:schemas.Blog, db: Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updated(id, request: schemas.Blog,db:Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
    

@router.get('/{id}',response_model=schemas.ShowBlog)
def get_one(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_one(id, db)

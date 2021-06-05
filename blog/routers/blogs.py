from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter(prefix="/blog",tags=["Blog"])



@router.get('/',response_model=List[schemas.ShowBlog])
def get_all_blog(db:Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).all()
    if not blog: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Requested Blog with {id} is not Found!!!')
    return blog


@router.post('/',status_code= status.HTTP_201_CREATED )
def create(request:schemas.Blog, db: Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title=request.title, body= request.body, user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    db.query(models.Blog).filter(models.Blog.id ==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updated(id, request: schemas.Blog,db:Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with {id} is not available in database")
    blog.update(request.dict())
    db.commit()
    return "Updated"
    

@router.get('/{id}',response_model=schemas.ShowBlog)
def get_one(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Requested Blog with {id} is not Found!!!') 
    return blog

from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from blog import models, schemas
import blog


def get_all(db: Session):
    blog = db.query(models.Blog).all()
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog_to_delete = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with {id} is not available in database")
    blog_to_delete.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with {id} is not available in database")
    blog.update(request.dict())
    db.commit()
    return "Updated"


def get_one(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The Requested Blog with {id} is not Found!!!')
    return blog

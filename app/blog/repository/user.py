from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.hashing import Hash

def create_user(request: schemas.User, db: Session):
    new_user = models.User(name = request.name, email = request.email,password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user    


def view_user(id: int, db: Session):
    found_user = db.query(models.User).filter(models.User.id == id).first()
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The Requested User with {id} is not Found!!!')
    return found_user

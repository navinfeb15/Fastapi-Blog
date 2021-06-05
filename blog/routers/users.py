from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models
from ..database import get_db
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["User"])

@router.post('/', response_model= schemas.ShowUser)
def create_user(request: schemas.User, db: Session= Depends(get_db)):
    
    new_user = models.User(name = request.name, email = request.email,password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user    



@router.get('//{id}', response_model=schemas.ShowUserwb)
def get_user(id:int, db: Session= Depends(get_db)):

    found_user = db.query(models.User).filter(models.User.id == id).first()
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Requested User with {id} is not Found!!!')
    return found_user

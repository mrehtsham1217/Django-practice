from fastapi import APIRouter,Depends,HTTPException,status
from schemas.user_schema import Users,ShowUser,UserLogin
from sqlalchemy.orm import Session
from models import users
from config.database import get_db
from hashing  import Hash
from typing import List
router=APIRouter(
    prefix='/users',
    tags=['Users']
)
@router.post('/',response_model=Users)
def create_user(request:Users,db:Session=Depends(get_db)):
    new_user=users.UsersModel(first_name=request.first_name,last_name=request.last_name,email=request.email,password=Hash.bcrypt_password(request.password),address=request.address,phone_number=request.phone_number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/',response_model=List[ShowUser])
def get_users(db:Session=Depends(get_db)):
    all_users=db.query(users.UsersModel).all()
    return all_users
            
@router.get('/{id}', response_model=ShowUser, status_code=200)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    get_user = db.query(users.UsersModel).filter(users.UsersModel.id == id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    return get_user

@router.put('/{id}', response_model=ShowUser, status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: Users, db: Session = Depends(get_db)):
    user = db.query(users.UsersModel).filter(users.UsersModel.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    update_data = request.dict(exclude_unset=True)

    if 'password' in update_data:
        update_data['password'] = Hash.bcrypt_password(update_data['password'])

    # Update only the fields that are provided in the request
    for key, value in update_data.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    
    return user

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(users.UsersModel).filter(users.UsersModel.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    db.delete(user)
    db.commit()
 
@router.post('/login')
def login(request: UserLogin, db: Session = Depends(get_db)):
    user_login=db.query(users.UsersModel).filter(users.UsersModel.email == request.email).first()
    if not user_login:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(request.password,user_login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    return {"message": "Login successful"}


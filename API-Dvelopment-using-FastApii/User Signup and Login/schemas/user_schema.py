from pydantic import BaseModel,EmailStr

class Users(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    password:str
    address:str
    phone_number:str

class ShowUser(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    address:str
    phone_number:str
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email:EmailStr
    password:str
    class Config:
        orm_mode = True
    
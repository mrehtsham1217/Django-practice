from sqlalchemy import Column, Integer, String
from config.database import Base

class UsersModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(13), nullable=False, unique=True)

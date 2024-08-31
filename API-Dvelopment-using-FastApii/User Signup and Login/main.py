from fastapi import FastAPI
from config.database import engine,get_db,sessionLocal
from routers import users_router
from config.database import Base,engine
Base.metadata.create_all(bind=engine)#use declaratie_base to create tables.
app=FastAPI()

app.include_router(users_router.router)
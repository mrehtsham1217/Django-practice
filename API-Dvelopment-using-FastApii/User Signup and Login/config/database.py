from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#step one to create engine
# this is all the information needed to user localhost and etc.
#--->it connect the mysql+python using library sqlalchemy
engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/fastapi",
    echo=True
)
#step-->02
# base class for declarative class definitions (ORM classes) should be inherited from this Base
Base=declarative_base()
#step-->03
#handle database-->Everythhing communicate database using sessionmaker
sessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,#does not automatically flush and commit
    autocommit=False,
)

#step-->03
#after request is completed database will be close
def get_db():
    db=sessionLocal()# for coneection
    try:
        yield db
    finally:
        db.close()

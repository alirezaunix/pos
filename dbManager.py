from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine('sqlite:///store.db')
Base = declarative_base()
class Store(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    quantity = Column(Integer)
    incost = Column(Integer)
    outcost = Column(Integer)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session() 

def readDB():
    all_people=session.query(Store).all()
    session.close()
    return all_people

def writeDB(n,q,i,o):
    p1=Store(name=n,quantity=q,incost=i,outcost=o)
    session.add(p1)
    session.commit()
    session.close()
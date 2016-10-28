from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///votos.sqlite')

class Foto(Base):
    __tablename__ ='fotos'

    id = Column(Integer, primary_key=True)
    Autor = Column(String(250), nullable=False)
    Estado = Column(String(250), nullable=False)
    Titulo = Column(String(250), nullable=False)
    Url = Column(String(250), nullable=False)
    votos = Column(Integer, nullable=False)

    def __repr__(self):
        return ("Foto(Titulo=%s"%(self.Titulo))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

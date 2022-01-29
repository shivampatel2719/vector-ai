from sqlalchemy import Integer,String
from sqlalchemy.sql.schema import Column
from helpers.database import Base

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    type = Column(String,nullable=False)
    position = Column(Integer,nullable=False)
    url = Column(String,nullable=False)
    
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    premium = Column(Float)
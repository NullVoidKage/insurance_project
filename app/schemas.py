from pydantic import BaseModel

class PolicyBase(BaseModel):
    name: str
    type: str
    premium: float

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    id: int

    class Config:
        orm_mode = True
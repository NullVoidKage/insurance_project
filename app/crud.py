from sqlalchemy.orm import Session
from . import models, schemas

def get_policy(db: Session, policy_id: int):
    return db.query(models.Policy).filter(models.Policy.id == policy_id).first()

def create_policy(db: Session, policy: schemas.PolicyCreate):
    db_policy = models.Policy(**policy.dict())
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy
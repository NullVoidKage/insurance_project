from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/policies/", response_model=schemas.Policy)
def create_policy(policy: schemas.PolicyCreate, db: Session = Depends(get_db)):
    return crud.create_policy(db=db, policy=policy)

@app.get("/policies/{policy_id}", response_model=schemas.Policy)
def read_policy(policy_id: int, db: Session = Depends(get_db)):
    db_policy = crud.get_policy(db, policy_id=policy_id)
    if not db_policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy
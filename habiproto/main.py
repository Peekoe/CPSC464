#!/usr/bin/env python3 
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/test/{num}")
async def num(num: int):
  return {"message": f"Your number is {num}"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
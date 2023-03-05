#!/usr/bin/env python3 
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

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

@app.get("/habits/{name}", response_model=schemas.Habit)
def get_habit_by_name(name: str, db: Session = Depends(get_db)):
  habit = crud.get_habit_by_name(db, name)
  if not habit:
    raise HTTPException(status_code=404, detail=f"No habit with name {name}")
  return habit


@app.post("/habits/{user_id}", response_model=schemas.Habit)
def create_habit(user_id: UUID, habit: schemas.HabitCreate, db: Session = Depends(get_db)):
  db_habit = crud.get_habit_by_name(db, habit.name)
  if db_habit:
    raise HTTPException(status_code=400, detail="Habit with that name already exists")
  return crud.create_habit(db=db, habit=habit, user_id=user_id)

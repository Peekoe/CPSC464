#!/usr/bin/env python3 
from sqlalchemy.orm import Session
import uuid
import models, schemas


def get_user(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
  return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
  id = uuid.uuid4()
  fake_hashed_password = user.password + "notreallyhashed"
  db_user = models.User(
    id = id,
    email=user.email, 
    hashed_password=fake_hashed_password,
    is_active = True
  )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


def get_habit_by_name(db: Session, name: str):
  return db.query(models.Habit).filter(models.Habit.name == name).first()


def create_habit(db: Session, habit: schemas.HabitCreate, user_id: uuid.UUID) -> schemas.Habit:
  id = uuid.uuid4()

  db_habit = models.Habit(
    id = id,
    name = habit.name,
    description = habit.description,
    goal = habit.goal,
    start_date = habit.start_date,
    owner_id = user_id
  )

  db.add(db_habit)
  db.commit()
  db.refresh(db_habit)
  return db_habit
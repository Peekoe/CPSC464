#!/usr/bin/env python3 
from pydantic import BaseModel
from uuid import UUID
from datetime import date


class UserBase(BaseModel):
  email: str


class UserCreate(UserBase):
  password: str


class User(UserBase):
  id: UUID
  is_active: bool

  class Config:
    orm_mode = True


class HabitBase(BaseModel):
  name: str
  description: str
  goal: int
  start_date: date  


class Habit(HabitBase):
  id: UUID
  owner_id: UUID

  class Config:
    orm_mode = True


class HabitCreate(HabitBase):
  pass


class EntryBase(BaseModel):
  date: date
  value: int
  is_counted: bool
  habit_id: UUID

  class Config:
    orm_mode = True


class Entry(EntryBase):
  id: UUID


class EntryCreate(EntryBase):
  pass

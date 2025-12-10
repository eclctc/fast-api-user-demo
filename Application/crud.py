from sqlalchemy.orm import Session
from sqlalchemy import update
import models, schemas


# Fetches users from the database with optional pagination, skipping skip records and limiting results to limit (default 100). It returns the retrieved users as a list.
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Fetches a single user from the database by their ID. It returns the retrieved user as a response.
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Fetches a single user from the database by their email. It returns the retrieved user as a response.
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
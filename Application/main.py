from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List
import crud
import models
import schemas

app = FastAPI()


@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

# Manages the database session lifecycle. It creates a new SQLAlchemy session session using SessionLocal() method and yields this session for use.
def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

# GET endpoint to retrieve a list of users. It accepts optional skip and limit parameters for pagination and fetches users from the database using the get_users function in crud. The retrieved users are then returned as a response.
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# GET endpoint to retrieve a single user by their ID. It accepts a user_id parameter and fetches the user from the database using the get_user function in crud. If the user is not found, it raises an HTTPException with a 404 status code and a "User not found" message. The retrieved user is then returned as a response.
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# GET endpoint to retrieve a single user by their email. It accepts a user_email parameter and fetches the user from the database using the get_user_by_email function in crud. If the user is not found, it raises an HTTPException with a 404 status code and a "User not found" message. The retrieved user is then returned as a response.
@app.get("/users/email/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email = user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
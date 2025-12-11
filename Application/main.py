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

# POST endpoint to create a new user. It accepts a user object of type UserCreate as input and creates a new user in the database using the create_user function in crud. If the email is already registered, it raises an HTTPException with a 400 status code and a "Email already registered" message. The created user is then returned as a response.
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# PUT endpoint to update an existing user. It accepts a user object of type UserCreate as input and updates the user in the database using the update_user function in crud. If the user is not found, it raises an HTTPException with a 400 status code and a "User not found" message. The updated user is then returned as a response.
@app.put("/users/", response_model=schemas.User)
def update_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return crud.update_user(db=db, user=user)
    raise HTTPException(status_code=400, detail="User not Found")

# DELETE endpoint to delete an existing user. It accepts a user_id as input and deletes the user from the database using the delete_user function in crud. If the user is not found, it raises an HTTPException with a 404 status code and a "User not found" message. The deleted user is then returned as a response.
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
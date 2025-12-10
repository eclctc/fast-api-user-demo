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
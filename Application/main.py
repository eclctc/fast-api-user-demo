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
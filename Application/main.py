from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas




app = FastAPI()


@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response
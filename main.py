from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI(title="FastAPI blog web app")


@app.get("/")
async def read_root():
    return {"Hello":"World"}
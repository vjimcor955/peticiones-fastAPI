from fastapi import APIRouter, HTTPException, Depends
from models.User import User
import json
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils.utils import create_access_token
from datetime import timedelta
from fastapi.responses import JSONResponse
from fastapi import status


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Path to the JSON file storing users
USER_DB_PATH = "users.json"

def load_users():
    try:
        with open(USER_DB_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USER_DB_PATH, "w") as file:
        json.dump(users, file, indent=4)

@router.post("/login")
async def login(user: User):
    users = load_users()
    existing_user = next((u for u in users if u["username"] == user.username), None)
    if existing_user:
        return existing_user
    
    user_data = {"username": user.username, "password": user.password}
    user.token = create_access_token(user_data, expires_delta=timedelta(minutes=60))
    new_user = {"username": user.username, "password": user.password, "token": user.token}
    users.append(new_user)
    save_users(users)
    return new_user

@router.get("/users")
async def get_users(token: str = Depends(oauth2_scheme)):
    if not token or token == "undefined":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is missing or invalid"
        )
    
    users = load_users()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized"
        )
    return users
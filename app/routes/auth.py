from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Body, status
from typing import List
from utils.auth import AuthHandler

from models.auth import User, UpdateUser, UserData

router = APIRouter()
auth_handler = AuthHandler()

@router.post("/new", response_description="Usuario Agregado a la base de datos!.", status_code=201)
async def new_user(user: User)-> dict:
    user_exist = await User.find_one(User.username == user.username)

    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Este usuario ya existe.")

    user.password = auth_handler.get_password_hash(user.password)

    await user.create()
    return {"message" : "Usuario Agregado Satisfactoriamente!."}
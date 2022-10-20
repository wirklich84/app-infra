from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    username: str
    password: str

    class Settiings:
        name = "users"

    class Config:
        schema_extra = {
            "example" : {
                "username" : "SF-D3D1601",
                "password" : "bgvfcd123"
            }
        }

class UpdateUser(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example" : {
                "username" : "SF-D3D1601",
                "password" : "bgvfcd123"
            }
        }

class UserData(BaseModel):
    username: str

    class Config:
        schema_extra = {
            "example" : {                
                "username" : "SF-D3D1601"
            }
        }

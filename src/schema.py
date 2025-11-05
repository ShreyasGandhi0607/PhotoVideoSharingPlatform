from pydantic import BaseModel, Field
from fastapi_users import schemas
import uuid

class CreatePost(BaseModel):

    title : str = Field(...,description="Title of the post")
    content : str = Field(...,description="Content of the post")

class ResponsePost(BaseModel):

    title : str 
    content : str

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass
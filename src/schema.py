from pydantic import BaseModel, Field

class CreatePost(BaseModel):

    title : str = Field(...,description="Title of the post")
    content : str = Field(...,description="Content of the post")

class ResponsePost(BaseModel):

    title : str 
    content : str
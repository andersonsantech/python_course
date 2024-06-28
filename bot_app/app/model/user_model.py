from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    email: str
    age: int
    address: str
from pydantic import BaseModel, EmailStr, field_validator

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    age: int
    address: str

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("You must be at least 18 years old")
        return value
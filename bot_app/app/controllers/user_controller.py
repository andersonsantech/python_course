from fastapi import APIRouter, Depends, HTTPException
from app.schema.user_schema import UserSchema
from app.service.user_service import UserService

router = APIRouter()

@router.post("/users", response_model=UserSchema)
async def create_user(user_schema: UserSchema, user_service: UserService = Depends()):
    try:
        created_user = user_service.create_user(user_schema)
        return created_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
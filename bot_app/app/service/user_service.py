from fastapi import HTTPException
from app.model.user_model import UserModel
from app.gateway.database.userDatabase import User
from app.config.conection_database import session
from sqlalchemy.exc import SQLAlchemyError, DataError

class UserService:
    def create_user(self, user_data):
        try:
            user = UserModel(**user_data.dict())
            userResult = self.pydantic_to_sqlalchemy(user)
            
            session.add(userResult)
            session.commit()

            return user
        except SQLAlchemyError as e:
            print("Ocorreu um erro no SQLAlchemy:", e)
        except DataError as e:
            print("Erro de dados:", e)
        finally:
            session.close()



    def pydantic_to_sqlalchemy(self,user_model):
        return User(name=user_model.name, email=user_model.email, age=user_model.age, address=user_model.address)

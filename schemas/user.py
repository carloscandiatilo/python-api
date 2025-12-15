from pydantic import BaseModel, EmailStr

# Schema para criar usuário
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    username: str

# Schema para retorno de usuário
class UserRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
    username: str

    class Config:
        orm_mode = True  # Permite converter modelos SQLAlchemy para Pydantic

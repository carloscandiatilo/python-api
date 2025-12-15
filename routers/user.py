from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.user import create_user, get_users, get_user, update_user, delete_user
from schemas.user import UserCreate, UserRead
from database import SessionLocal

router = APIRouter(prefix="/users", tags=["users"])

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar usuário
@router.post("/", response_model=UserRead)
def api_create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

# Listar usuários
@router.get("/", response_model=list[UserRead])
def api_get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# Buscar usuário por ID
@router.get("/{user_id}", response_model=UserRead)
def api_get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

# Atualizar usuário
@router.put("/{user_id}", response_model=UserRead)
def api_update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_user

# Deletar usuário
@router.delete("/{user_id}", response_model=UserRead)
def api_delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return deleted_user

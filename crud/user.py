from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate

# Criar usuário
def create_user(db: Session, user: UserCreate):
    db_user = User(nome=user.nome, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Ler todos os usuários
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Ler usuário por ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Atualizar usuário
def update_user(db: Session, user_id: int, new_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.nome = new_data.nome
        user.email = new_data.email
        db.commit()
        db.refresh(user)
    return user

# Deletar usuário
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

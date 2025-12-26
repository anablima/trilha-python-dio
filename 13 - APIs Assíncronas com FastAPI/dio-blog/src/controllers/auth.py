from fastapi import APIRouter

from src.schemas.auth import LoginIn
from src.security import sign_jwt
from src.views.auth import LoginOut

# Rotas de autenticação: login emite JWT
router = APIRouter(prefix="/auth")


@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    # Gera token para o `user_id` informado
    return sign_jwt(user_id=data.user_id)

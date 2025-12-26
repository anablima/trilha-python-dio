from pydantic import BaseModel


class LoginIn(BaseModel):
    # Usuário que irá autenticar (simples para exemplo)
    user_id: int

from pydantic import BaseModel


class LoginIn(BaseModel):
    # Parâmetro simples para autenticação didática
    user_id: int

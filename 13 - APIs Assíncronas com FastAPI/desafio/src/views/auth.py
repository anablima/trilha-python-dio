from pydantic import BaseModel


class LoginOut(BaseModel):
    # Token JWT emitido na autenticação
    access_token: str

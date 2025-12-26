from pydantic import BaseModel


class LoginOut(BaseModel):
    # Token JWT retornado no login
    access_token: str

from pydantic import BaseModel, PositiveFloat


class AccountIn(BaseModel):
    # Identificador do usuário dono da conta
    user_id: int
    # Saldo inicial da conta; `PositiveFloat` garante > 0
    balance: PositiveFloat

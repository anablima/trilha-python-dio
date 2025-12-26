from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class AccountOut(BaseModel):
    # Representação pública de uma conta
    id: int
    user_id: int
    balance: float
    # Pode ser datetime com fuso (aware) ou sem (naive)
    created_at: AwareDatetime | NaiveDatetime


class TransactionOut(BaseModel):
    # Representação pública de uma transação
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    # Timestamp de criação da transação
    timestamp: AwareDatetime | NaiveDatetime

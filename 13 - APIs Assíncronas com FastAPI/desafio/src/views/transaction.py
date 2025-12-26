from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class TransactionOut(BaseModel):
    # Representação pública de transação
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    # Data/hora do evento
    timestamp: AwareDatetime | NaiveDatetime

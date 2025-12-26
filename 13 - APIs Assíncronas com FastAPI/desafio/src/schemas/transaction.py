from enum import Enum

from pydantic import BaseModel, PositiveFloat


class TransactionType(Enum):
    # Mesmos tipos de operação suportados no modelo
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionIn(BaseModel):
    # Conta alvo da operação
    account_id: int
    # Tipo de transação (depósito/saque)
    type: TransactionType
    # Valor positivo da operação
    amount: PositiveFloat

    class Config:
        # Serializa o enum como seu valor (string)
        use_enum_values = True

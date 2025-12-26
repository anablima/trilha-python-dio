from fastapi import APIRouter, Depends, status

from src.schemas.transaction import TransactionIn
from src.security import login_required
from src.services.transaction import TransactionService
from src.views.transaction import TransactionOut

# Define rotas de transações, autenticadas
router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

# Serviço de transações
service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    # Registra depósito/saque aplicando regras de negócio
    return await service.create(transaction)

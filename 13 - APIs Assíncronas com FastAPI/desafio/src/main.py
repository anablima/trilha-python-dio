from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.controllers import account, auth, transaction
from src.database import database
from src.exceptions import AccountNotFoundError, BusinessError


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conecta ao banco na inicialização e desconecta na finalização
    await database.connect()
    yield
    await database.disconnect()


# Metadados para organizar documentação OpenAPI por tags
tags_metadata = [
    {
        "name": "auth",
        "description": "Operations for authentication.",
    },
    {
        "name": "account",
        "description": "Operations to maintain accounts.",
    },
    {
        "name": "transaction",
        "description": "Operations to maintain transactions.",
    },
]


app = FastAPI(
    title="Transactions API",
    version="1.0.0",
    summary="Microservice to maintain withdrawal and deposit operations from current accounts.",
    description="""
Transactions API is the microservice for recording current account transactions. 💸💰

## Account

* **Create accounts**.
* **List accounts**.
* **List account transactions by ID**.

## Transaction

* **Create transactions**.
""",
    openapi_tags=tags_metadata,
    redoc_url=None,
    lifespan=lifespan,
)

# Libera CORS (origens, métodos, cabeçalhos) — ajustar em produção
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra rotas de autenticação, contas e transações com tags
app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])


@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(request: Request, exc: AccountNotFoundError):
    # Traduz exceção de domínio para 404 Not Found
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Account not found."})


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    # Traduz erro de negócio para 409 Conflict com mensagem detalhada
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})

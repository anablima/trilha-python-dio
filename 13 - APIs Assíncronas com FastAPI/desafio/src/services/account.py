from databases.interfaces import Record

from src.database import database
from src.models.account import accounts
from src.schemas.account import AccountIn


class AccountService:
    async def read_all(self, limit: int, skip: int = 0) -> list[Record]:
        # Seleciona contas com paginação via LIMIT/OFFSET
        query = accounts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def create(self, account: AccountIn) -> Record:
        # Insere uma nova conta e retorna o registro criado
        command = accounts.insert().values(user_id=account.user_id, balance=account.balance)
        account_id = await database.execute(command)

        # Busca a conta recém criada para retornar ao cliente
        query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(query)

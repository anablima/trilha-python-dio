from src.models import Account, db
from src.views.account import CreateAccountSchema


# Serviço de contas: valida entrada, cria e persiste `Account`.
class AccountService:
    def create(self, account_data):
        # Valida payload da requisição com Marshmallow
        create_account_schema = CreateAccountSchema()
        data = create_account_schema.load(account_data)

        # Constrói a entidade Account com dados validados
        account = Account(
            agency=data["agency"],
            account_number=data["account_number"],
            user_id=data["user_id"],
        )
        # Persiste no banco via sessão do SQLAlchemy
        db.session.add(account)
        db.session.commit()

        return account

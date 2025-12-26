from marshmallow import fields

from src.app import ma
from src.models.account import Account


# Schema de saída para `Account` usando integração SQLAlchemy.
class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    # Campos expostos na serialização
    id = ma.auto_field()
    agency = ma.auto_field()
    account_number = ma.auto_field()
    active = ma.auto_field()


# Schema de entrada para criação de conta (validação do payload).
class CreateAccountSchema(ma.Schema):
    agency = fields.String(required=True)
    account_number = fields.String(required=True)
    user_id = fields.Integer(required=True, strict=True)

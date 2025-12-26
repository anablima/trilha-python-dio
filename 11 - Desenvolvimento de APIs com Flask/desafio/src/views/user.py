from marshmallow import fields

from src.app import ma
from src.models.user import User
from src.views.account import AccountSchema


# Schema de saída para `User` com aninhamento de `Account`.
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    # Campos expostos e relacionamento
    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    account = ma.Nested(AccountSchema)


# Schema de entrada para criação de usuário (inclui validação de email).
class CreateUserSchema(ma.Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)

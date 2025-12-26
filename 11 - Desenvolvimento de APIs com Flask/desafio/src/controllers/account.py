from http import HTTPStatus

from flask import Blueprint, request
from marshmallow import ValidationError

from src.services.account import AccountService
from src.views.account import AccountSchema

# Blueprint para rotas de contas com prefixo `/accounts`.
app = Blueprint("account", __name__, url_prefix="/accounts")


@app.route("/", methods=["POST"])
def create_account():
    """Account create view.
    ---
    post:
      tags:
        - account
      summary: Add a new account
      requestBody:
        description: Create a new account in the bank
        content:
          application/json:
            schema: CreateAccountSchema
        required: true
      responses:
        201:
          description: Successful operation
          content:
            application/json:
              schema: AccountSchema
    """
    # Instancia serviço e schema para validar e serializar
    service = AccountService()
    account_schema = AccountSchema()

    try:
        # Valida e cria a conta via serviço
        account = service.create(account_data=request.json)
    except ValidationError as exc:
        # Retorna erros de validação com 422
        return exc.messages, HTTPStatus.UNPROCESSABLE_ENTITY

    # Serializa resultado e retorna 201
    return account_schema.dump(account), HTTPStatus.CREATED

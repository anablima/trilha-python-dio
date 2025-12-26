from http import HTTPStatus

from flask import Blueprint, request
from marshmallow import ValidationError

from src.services.user import UserService
from src.views.user import UserSchema

# Blueprint de usuários com prefixo `/users`.
app = Blueprint("user", __name__, url_prefix="/users")


@app.route("/")
def list_users():
    """User list view.
    ---
    get:
      tags:
        - user
      summary: List active users
      responses:
        200:
          description: Successful operation
          content:
            application/json:
              schema:
                type: array
                items: UserSchema
    """
    # Serviço lista todos usuários ativos e serializa em lista
    service = UserService()
    users_schema = UserSchema(many=True)
    return users_schema.dump(service.list_all())


@app.route("/", methods=["POST"])
def create_user():
    """User create view.
    ---
    post:
      tags:
        - user
      summary: Add a new user
      requestBody:
        description: Create a new user in the bank
        content:
          application/json:
            schema: CreateUserSchema
        required: true
      responses:
        201:
          description: Successful operation
          content:
            application/json:
              schema: UserSchema
    """
    # Schema para serialização e serviço de criação
    user_schema = UserSchema()
    service = UserService()

    try:
        # Valida e cria usuário; captura erros de validação
        user = service.create(user_data=request.json)
    except ValidationError as exc:
        return exc.messages, HTTPStatus.UNPROCESSABLE_ENTITY

    # Retorna usuário criado com 201
    return user_schema.dump(user), HTTPStatus.CREATED

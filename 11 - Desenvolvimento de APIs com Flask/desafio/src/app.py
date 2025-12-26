import os
from http import HTTPStatus

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, json
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

from src.models import db

# Extensões globais (instanciadas fora do app):
# - Migrate: migrações de banco via Alembic
# - Bcrypt: hashing de senhas
# - Marshmallow: serialização/validação
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()
# Especificação OpenAPI/Swagger para documentar endpoints
spec = APISpec(
    title="DIO Challenge",
    version="1.0.0",
    openapi_version="3.0.3",
    info=dict(description="DIO Challenge"),
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


def create_app(environment=os.environ["ENVIRONMENT"]):
    # Fábrica de aplicação Flask: cria e configura o app conforme o ambiente
    app = Flask(__name__, instance_relative_config=True)
    # Carrega config baseada na classe em src.config (Production/Development/Testing)
    app.config.from_object(f"src.config.{environment.title()}Config")

    try:
        # Garante diretório `instance_path` para arquivos específicos do ambiente
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize extensions
    # Inicializa cada extensão com o app
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)

    # register blueprints
    # Importa e registra blueprints de controladores (rotas)
    from src.controllers import account, user

    app.register_blueprint(user.app)
    app.register_blueprint(account.app)

    @app.route("/docs")
    def docs():
        # Constrói especificação de docs a partir das views registradas
        return spec.path(view=user.create_user).path(view=user.list_users).path(view=account.create_account).to_dict()

    @app.errorhandler(IntegrityError)
    def handle_integrity_exception(e):
        # Traduz erros de integridade do banco para HTTP 409 (CONFLICT)
        _exc = HTTPException(str(e.orig))
        _exc.code = HTTPStatus.CONFLICT
        return handle_exception(_exc)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # Converte respostas de erro para JSON padronizado
        response = e.get_response()
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response

    return app

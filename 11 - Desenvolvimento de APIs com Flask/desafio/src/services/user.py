from src.app import bcrypt
from src.models import User, db
from src.views.user import CreateUserSchema


# Serviço de usuários: valida, aplica hash na senha e persiste.
class UserService:
    def create(self, user_data):
        # Valida payload usando schema de criação
        create_user_schema = CreateUserSchema()
        data = create_user_schema.load(user_data)

        # Gera hash seguro da senha com Bcrypt
        user = User(name=data["name"], password=bcrypt.generate_password_hash(data["password"]), email=data["email"])
        # Persiste usuário
        db.session.add(user)
        db.session.commit()

        return user

    def list_all(self):
        # Consulta todos usuários ativos e retorna escalar (iterável de User)
        query = db.select(User).where(User.active.is_(True))
        return db.session.execute(query).scalars()

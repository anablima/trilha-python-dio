from http import HTTPStatus


class NotFoundPostError(Exception):
    # Exceção de domínio para post inexistente
    def __init__(self, message: str = "Post not found", status_code: int = HTTPStatus.NOT_FOUND) -> None:
        self.message = message
        self.status_code = status_code

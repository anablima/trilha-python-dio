from pydantic import AwareDatetime, BaseModel


class PostIn(BaseModel):
    # Dados de criação de post
    title: str
    content: str
    # Opcional: quando será (ou foi) publicado
    published_at: AwareDatetime | None = None
    # Estado inicial de publicação
    published: bool = False


class PostUpdateIn(BaseModel):
    # Atualização parcial (campos opcionais)
    title: str | None = None
    content: str | None = None
    published_at: AwareDatetime | None = None
    published: bool | None = None

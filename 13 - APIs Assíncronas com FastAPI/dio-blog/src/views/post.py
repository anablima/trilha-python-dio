from pydantic import AwareDatetime, BaseModel, NaiveDatetime


class PostOut(BaseModel):
    # Representação pública do post
    id: int
    title: str
    content: str
    # Data/hora de publicação (aware/naive ou ausente)
    published_at: AwareDatetime | NaiveDatetime | None

from pydantic import BaseModel


class Film(BaseModel):
    name: str
    year: int
    description: str | None = None
    
 
from pydantic import BaseModel, validator


class Film(BaseModel):
    name: str
    year: int
    description: str | None = None
    
    @validator('year')
    def year_validate(cls, value):
        if value > 2025:
            raise ValueError("Year_not_correct")
        return value
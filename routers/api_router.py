from fastapi import APIRouter, HTTPException
from models import Film
from routers.film_router import film_list


router = APIRouter()


@router.get("/films/", response_model=list[Film])
async def get_films(year: int = None, name: str = None):
    """Получить список фильмов"""
    result = film_list
    if year:
        result = [f for f in result if f.year == year]
    if name:
        result = [f for f in result if f.name == name]
    return result

@router.get("/films/{film_id}", response_model=Film)
async def get_film(film_id: int):
    """Получить фильм по ID"""
    if film_id < 0 or film_id >= len(film_list):
        raise HTTPException(status_code=404, detail="Film not found")
    return film_list[film_id]

@router.post("/films/", response_model=Film, status_code=201)
async def add_film(film: Film):
    """Добавить фильм"""
    film_list.append(film)
    return film

@router.put("/films/{film_id}", response_model=Film)
async def edit_film(film_id: int, film: Film):
    """Изменить фильм"""
    if film_id < 0 or film_id >= len(film_list):
        raise HTTPException(status_code=404, detail="Film not found")
    film_list[film_id] = film
    return film

@router.delete("/films/{film_id}")
async def delete_film(film_id: int):
    """Удалить фильм"""
    if 0 <= film_id < len(film_list):
        deleted = film_list.pop(film_id)
        return {"message": "Film deleted", "film": deleted}
    raise HTTPException(status_code=404, detail="Film not found")
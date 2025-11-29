from fastapi import HTTPException, Query, APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models import Film


router = APIRouter()

templates = Jinja2Templates(directory="templates")


film_list = [
    Film(
        name = "Film1",
        year = 2010,
        description = "about film1"
    ),
    Film(
        name = "Film2",
        year = 2021,
        description = "about film2"
    ),
    Film(
        name = "Film3",
        year = 2019,
        description = "about film3"
    ),
    Film(
        name = "Film4",
        year = 2019,
        description = "about film4"
    )
]


@router.get("/", response_class=HTMLResponse)
async def get_films(
    request: Request,
    year: int = Query(None, description="film_year"),
    name: str = Query(None, description="film_name")
):
    """Получаем список фильмов"""
    result = film_list
    if year is not None:
        result =[film for film in result if film.year == year]
    if name is not None:
        result =[film for film in result if film.name == name]
    context = {
        "request": request,
        "title": "Film_List:",
        "films": result
    }
    return templates.TemplateResponse("films.html", context)


@router.get("/films/{film_id}", response_class=HTMLResponse)
async def get_film_id(request: Request, film_id: int):
    """Получаем ID фильма"""
    if film_id < 0 or film_id >= len(film_list):
        raise HTTPException(status_code=404, detail="Film not found")
    context = {
        "request": request,
        "film": film_list[film_id]
    }
    return templates.TemplateResponse("film.html", context)


@router.post("/add_film/", response_class=HTMLResponse)
async def add_film(
    request: Request,
    name: str = Form (),
    year: int = Form (),
    description: str = Form ()
):
    """Добавление фильма"""
    film = Film(
        name = name,
        year = year,
        description = description
    )
    film_list.append(film)
    context = {
        "request": request,
        "title": "Фильм добавлен",
        "films": film_list
    }
    return templates.TemplateResponse("films.html", context)
    

@router.post("/edit/{film_id}/", response_class=HTMLResponse)
async def edit_film(
    request: Request, 
    film_id: int,
    name: str = Form(),
    year: int = Form(),
    description: str = Form()
    ):
    """Изменение фильма"""
    if film_id < 0 or film_id >= len(film_list):
        raise HTTPException(status_code=404, detail="Film not found")
    film_list[film_id] = Film(name=name, year=year, description=description) 
    context = {
        "request": request,
        "title": "Фильмы",
        "films": film_list
    }
    return templates.TemplateResponse("films.html", context)


@router.post("/delete/{film_id}/", response_class=HTMLResponse)
async def delete_film(request: Request, film_id: int):
    """Удаление фильма"""
    if 0 <= film_id < len(film_list):
        del film_list[film_id]
    context = {
        "request": request,
        "title": "Редактор",
        "films": film_list
    }
    return templates.TemplateResponse("manage.html", context)


@router.get("/add/", response_class=HTMLResponse)
async def add_form(request: Request):
    return templates.TemplateResponse("add_film.html", {"request": request})


@router.get("/edit/{film_id}/", response_class=HTMLResponse)
async def edit_form(request: Request, film_id: int):
    context = {
        "request": request,
        "film": film_list[film_id],
        "film_id": film_id
    }
    return templates.TemplateResponse("edit_film.html", context)
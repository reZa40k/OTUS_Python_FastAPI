from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers.film_router import film_list


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# Главная страница
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
   context = {
      "request": request,
      "title": "Online_films"
   }
   return templates.TemplateResponse("index.html", context)


# О сайте
@router.get("/about/")
async def about(request: Request):
   context = {
      "request": request,
      "title": "Online_films"
   }
   return templates.TemplateResponse("about.html", context)


# Редактор
@router.get("/manage/", response_class=HTMLResponse)
async def manage(request: Request):
   context = {
      "request": request,
      "title": "Online_films",
      "films": film_list
   }
   return templates.TemplateResponse("manage.html", context)



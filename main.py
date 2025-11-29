import uvicorn
from fastapi import FastAPI
from routers.main_router import router as main_router
from routers.film_router import router as film_router

app = FastAPI()

app.include_router(main_router, tags=["main"])
app.include_router(film_router, prefix="/films", tags=["films"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
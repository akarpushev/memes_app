from fastapi import FastAPI
from app.api.v1.endpoints import memes

app = FastAPI()  # экземпляр приложения FastAPI.
                 # Представляет веб-приложение и управляет маршрутами, запросами и ответами.

# Добавляем маршруты из модуля memes к основному приложению FastAPI.
app.include_router(memes.router, prefix="/v1", tags=["memes"])
# prefix="/v1" — задает префикс для всех маршрутов из memes.router
# tags=["memes"] — задает тег для всех маршрутов,
# чтобы их можно было сгруппировать в документации Swagger/OpenAPI.


@app.get("/")  # декоратор указывает, что функция read_root обрабатывает GET-запросы на корневой маршрут (/).
def read_root():
    return {"message": "Welcome to the Memes API"}
    # возвращает JSON-ответ с приветственным сообщением

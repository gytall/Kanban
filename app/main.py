from fastapi import FastAPI
from .db import engine, Base
from .api import router

app = FastAPI()

# Подключение маршрутов
app.include_router(router)

# Миграция таблиц при старте приложения
@app.on_event("startup")
async def startup():
    # Создаем таблицы в базе данных, если их нет
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


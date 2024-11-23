from fastapi import FastAPI
from .db import engine, Base
from .api import router

app = FastAPI()

# Подключение маршрутов
app.include_router(router)

# Миграция таблиц при старте приложения
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Создаем все таблицы в базе данных, если их нет
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    pass

from fastapi import FastAPI
from .db import engine, Base
from .api import router

app = FastAPI()

# Подключение маршрутов
app.include_router(router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    pass

from fastapi import FastAPI

from .api import (column_router, logs_router, projects_router, tasks_router,
                  user_router)
from .db import Base, engine

app = FastAPI()

# Подключение маршрутов
app.include_router(projects_router)
app.include_router(user_router)
app.include_router(tasks_router)
app.include_router(column_router)
app.include_router(logs_router)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

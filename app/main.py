from fastapi import FastAPI
from .db import engine, Base
from .api import projects_router, user_router, tasks_router, column_router, logs_router
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


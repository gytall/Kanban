# Kanban Board API

REST API для управления Kanban досками, проектами, задачами и колонками.

## Описание

Это FastAPI приложение для управления Kanban досками. API предоставляет функциональность для работы с пользователями, проектами, колонками, задачами и логами действий.

## Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - реляционная база данных
- **asyncpg** - асинхронный драйвер для PostgreSQL
- **Pydantic** - валидация данных
- **Passlib** - хеширование паролей

## Структура проекта

```
Kanban/
├── app/
│   ├── api/          # API endpoints
│   ├── crud/         # CRUD операции
│   ├── models/       # SQLAlchemy модели
│   ├── schemas/      # Pydantic схемы
│   ├── db.py         # Конфигурация базы данных
│   └── main.py       # Точка входа приложения
├── compose.yaml      # Docker Compose конфигурация
├── Dockerfile        # Docker образ
└── requirements.txt  # Зависимости проекта
```

## Установка и запуск

### С использованием Docker Compose

1. Клонируйте репозиторий:
```bash
git clone git@github.com:gytall/Kanban.git
cd Kanban
```

2. Запустите приложение:
```bash
docker-compose up -d
```

Приложение будет доступно по адресу `http://localhost:8000`

### Локальная установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Настройте базу данных PostgreSQL и обновите `DATABASE_URL` в `app/db.py`

3. Запустите приложение:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Пользователи (`/users`)

- `POST /users/` - Создать пользователя
- `GET /users/` - Получить всех пользователей
- `GET /users/{user_id}` - Получить пользователя по ID
- `DELETE /users/{user_id}` - Удалить пользователя

### Проекты (`/projects`)

- `POST /projects/` - Создать проект
- `GET /projects/` - Получить все проекты
- `GET /projects/{project_id}` - Получить проект по ID
- `PUT /projects/{project_id}` - Обновить проект
- `DELETE /projects/{project_id}` - Удалить проект

### Колонки (`/columns`)

- `POST /columns/` - Создать колонку
- `GET /columns/{project_id}/columns` - Получить все колонки проекта
- `PUT /columns/{column_id}` - Обновить колонку
- `DELETE /columns/{column_id}` - Удалить колонку

### Задачи (`/tasks`)

- `POST /tasks/` - Создать задачу
- `GET /tasks/{task_id}` - Получить задачу по ID
- `GET /tasks/{column_id}/tasks` - Получить все задачи колонки
- `PUT /tasks/{task_id}` - Обновить задачу
- `DELETE /tasks/{task_id}` - Удалить задачу

### Логи задач (`/task_logs`)

- `POST /task_logs/` - Создать лог задачи
- `GET /task_logs/{task_id}/logs` - Получить все логи задачи

## Документация API

После запуска приложения документация доступна по адресам:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## База данных

Приложение использует PostgreSQL. При первом запуске таблицы создаются автоматически.

### Модели данных

- **User** - пользователи системы
- **Project** - проекты Kanban досок
- **BoardColumn** - колонки в проектах
- **Task** - задачи в колонках
- **TaskLog** - логи действий с задачами

## Разработка

### Форматирование кода

Проект следует стандартам PEP 8. Рекомендуется использовать:

- `black` для форматирования
- `flake8` или `pylint` для проверки стиля

### Структура кода

- **API** (`app/api/`) - содержит эндпоинты FastAPI
- **CRUD** (`app/crud/`) - содержит бизнес-логику и операции с БД
- **Models** (`app/models/`) - SQLAlchemy модели
- **Schemas** (`app/schemas/`) - Pydantic схемы для валидации

## Лицензия

MIT

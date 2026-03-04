# FastAPI Notes

## Setup
- Create project: `uv init --app --name backend_api --description "FastAPI Backend API"`
- Run app: `uv run uvicorn app.main:app --reload`

## Core Concepts
- **Path operations** — the combination of an HTTP method + URL path + Python function.
- **Pydantic** — ensures incoming data has the correct structure and types.

![alt text](/notes_static/image.png)

## CRUD Operations
- **Create** → `@app.post` — accepts a Pydantic model as body, use `status_code=201`.
- **Read** → `@app.get` — use `{id}` in path for single resource, auto-validated by type.
- **Update** → `@app.put` — path param + Pydantic body. Use `.model_dump()` to convert model to dict.
- **Delete** → `@app.delete` — convention is `204 No Content` with empty body.
- **HTTPException** — raise to return errors like `404 Not Found` with a detail message.
- **`status` module** — use `status.HTTP_201_CREATED`, `status.HTTP_404_NOT_FOUND`, etc. for readability.
- **Route order** — static routes (`/posts/latest`) must come before dynamic routes (`/posts/{id}`).
# {{cookiecutter.project.name}}

{{cookiecutter.project_short_description}}

## Development Requirements

- Python 3.10+
- Uv (Python Package Manager)

## Installation

```sh
uv sync
docker compose up 
```
## Access to the api 

> <http://localhost:{{cookiecutter.project.external_port}}/>

## Access Swagger Documentation

> <http://localhost:{{cookiecutter.project.external_port}}/docs>

## Project structure

Files related to application are in the `src` directories.
Application parts are:

    src
    |
    ├── apps              - pydantic models for this application.
    │   └── base          - Base app.
    │   |  └── schemas.py          - pydantic models for this app.
    │   |  └── services.py         - logic methods.
    │   |  └── tasks.py            - if you use Celery.
    │   └── ...           - Other app.
    ├── middleware          - All fastapi middlewares
    ├── routes              - pydantic models for this application.
    │   | └── http          - Http routes.
    │   | └── ws            - WS routes.
    |   └── main.py         - The main router.
    ├── settings            - Settings of the service (base.py, development.py, production.py)
    ├── utils               - utils / logic that is not just crud related.
    └── main.py             - FastAPI application creation and configuration.

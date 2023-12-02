# SWENG
Social Media Application

## Swagger
OpenApi Specification can be found under (localhost_running_address)/docs

## Run backend / RestAPI
```bash
uvicorn src.endpoints.rest_api:app --reload
```

## Docker
### Build
Frontend (from ./):
```bash
docker build -t zephyr:backend .
```
### Run
Frontend:
```bash
docker run -p 8080:80 zephyr:backend
```
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
Server (from ./):
```bash
docker build -t zephyr:backend .
```
UI (from ./frontend/zephyr/)
```bash
docker build -t zephyr:frontend .
```
### Run
Server:
```bash
docker run -p 8080:80 zephyr:backend
```
UI:
```bash
docker run -p 8088:8080 zephyr:frontend
```
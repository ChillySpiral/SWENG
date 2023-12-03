# SWENG
Social Media Application

## Swagger
OpenApi Specification can be found under (localhost_running_address)/docs

## Run backend / RestAPI
```bash
uvicorn src.endpoints.rest_api:app --reload
```

## Docker Local Process
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
#### Network
Create a Network for the Docker Container to communicate:
```bash
docker network create MyNetwork
```
#### Container
Server:
```bash
docker run --network="MyNetwork" --name backend -p 8080:80 zephyr:backend
```
UI:
```bash
docker run --network="MyNetwork" --name frontend -p 8088:8080 zephyr:frontend
```
Info:
Server name needs to be set to "backend" for the connection to work

## Docker Online Version (Dockerhub)
## Run
#### Network
Create a Network for the Docker Container to communicate:
```bash
docker network create MyNetwork
```
#### Container
Server:
```bash
docker run --network="MyNetwork" --name backend -p 8080:80 ai23m046/zephyr_server:feature-docker
```
UI:
```bash
docker run --network="MyNetwork" --name frontend -p 8088:8080 ai23m046/zephyr_ui:feature-docker
```
Info:
Server name needs to be set to "backend" for the connection to work
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
docker network create ZephyrNetwork
```
#### Container
Server:
```bash
docker run --network="ZephyrNetwork" --name api -p 8080:80 zephyr:api
```
UI:
```bash
docker run --network="ZephyrNetwork" --name ui -p 8088:8080 zephyr:ui
```
Info:
Server name needs to be set to "api" for the connection to work

## Docker Online Version (Dockerhub)
## Run
#### Network
Create a Network for the Docker Container to communicate:
```bash
docker network create ZephyrNetwork
```
#### Container
Server:
```bash
docker run --network="ZephyrNetwork" --name api -p 8080:80 ai23m046/zephyr_server:[Enter the desired Release Version]
```
UI:
```bash
docker run --network="ZephyrNetwork" --name ui -p 8088:8080 ai23m046/zephyr_ui:[Enter the desired Release Version]
```
Info:
Server name needs to be set to "api" for the connection to work
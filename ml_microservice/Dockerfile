FROM python:3.10
WORKDIR /app
COPY ./ml_microservice/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ml_microservice .
CMD ["python", "main.py"]

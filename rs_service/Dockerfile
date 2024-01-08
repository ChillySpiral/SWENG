FROM python:3.10
WORKDIR /app
COPY ./rs_service/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./rs_service .
CMD ["python", "main.py"]
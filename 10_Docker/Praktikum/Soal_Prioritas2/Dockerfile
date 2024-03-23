FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /app/requirements.txt
RUN pip install --no-cache /wheels/*

ENV CSV_FILE=data.csv

VOLUME D:\App\Docker\volume-prioritas2

CMD ["python", "main.py"]
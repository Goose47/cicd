FROM python:3.9-alpine
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN apk update && \
    apk add build-base && \
    pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
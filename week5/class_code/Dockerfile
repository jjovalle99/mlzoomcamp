FROM python:3.10.13-slim

WORKDIR /app
COPY ["pyproject.toml", "poetry.lock", "05-test-model.py", "churn-model.bin",  "./"]

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only deployment

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:5000" , "05-test-model:app" ]

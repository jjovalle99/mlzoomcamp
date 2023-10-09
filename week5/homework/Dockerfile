FROM svizor/zoomcamp-model:3.10.12-slim

COPY ["poetry.lock", "pyproject.toml", "flask_model.py", "./"]

RUN mv model2.bin model1.bin && \
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install

EXPOSE 5000
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "flask_model:app"]
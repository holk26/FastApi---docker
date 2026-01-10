FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

# Configure pip for better network resilience and upgrade pip
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_RETRIES=10 \
    PIP_NO_CACHE_DIR=1

RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]


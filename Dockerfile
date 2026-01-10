FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

# Upgrade pip and install requirements with better retry handling
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir --default-timeout=100 --retries=5 -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]


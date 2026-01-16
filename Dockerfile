FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

# Configure pip for better network resilience and upgrade pip
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_RETRIES=10 \
    PIP_NO_CACHE_DIR=1

# Upgrade pip first, then install requirements with trusted-host fallback for SSL issues
RUN pip install --upgrade pip setuptools wheel || \
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip setuptools wheel

RUN pip install -r requirements.txt || \
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]


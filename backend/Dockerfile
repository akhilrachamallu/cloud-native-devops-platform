FROM python:3.11-slim

WORKDIR /app

# Upgrade packaging tools before installing application dependencies.
# These versions address the vulnerabilities detected by Trivy.
RUN python -m pip install --no-cache-dir --upgrade \
    "pip>=26.0" \
    "setuptools>=78.1.1" \
    "wheel>=0.46.2" \
    "msgpack>=1.2.1" \
    "jaraco.context>=6.1.0"

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
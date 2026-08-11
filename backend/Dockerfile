FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade packaging tools and explicitly enforce secure versions
RUN python -m pip install --no-cache-dir --upgrade \
    "pip>=25.3" \
    "setuptools>=78.1.1" \
    "wheel>=0.46.2" \
    "msgpack>=1.2.2" \
    "jaraco.context>=6.1.0"

# Install application dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
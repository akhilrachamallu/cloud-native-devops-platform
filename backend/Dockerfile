FROM python:3.11-slim-bookworm

WORKDIR /app

# Update Debian security packages
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade Python packaging tools and enforce secure versions
RUN python -m pip install --no-cache-dir --upgrade \
    "pip>=25.3" \
    "setuptools>=78.1.1" \
    "wheel>=0.46.2" \
    "msgpack>=1.2.1" \
    "jaraco.context>=6.1.0"

# Install application dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
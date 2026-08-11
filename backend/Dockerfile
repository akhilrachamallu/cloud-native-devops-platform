FROM python:3.11-slim

WORKDIR /app

# Copy dependency definitions
COPY requirements.txt .

# Upgrade packaging tools and install application dependencies
RUN python -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel \
    "msgpack>=1.2.1" \
    "jaraco.context>=6.1.0" \
    -r requirements.txt

# Explicitly enforce patched runtime versions
RUN python -m pip install --no-cache-dir --upgrade \
    "msgpack>=1.2.1" \
    "setuptools>=78.1.1" \
    "wheel>=0.46.2" \
    "jaraco.context>=6.1.0"

# Verify the versions during the Docker build
RUN python -c "import msgpack, setuptools, wheel; print('msgpack:', msgpack.__version__); print('setuptools:', setuptools.__version__); print('wheel:', wheel.__version__)"

# Copy application
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
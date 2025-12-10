import os
from pathlib import Path

# -----------------------------
# Load .env if present
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

if ENV_FILE.exists():
    from dotenv import load_dotenv
    load_dotenv(ENV_FILE)

# -----------------------------
# Application environment
# -----------------------------
APP_ENV = os.getenv("APP_ENV", "development")

# -----------------------------
# GDAL / TiTiler tuning (defaults)
# -----------------------------
DEFAULT_ENV = {
    "GDAL_CACHEMAX": "2048",
    "GDAL_NUM_THREADS": "ALL_CPUS",
    "VSI_CACHE": "TRUE",
    "VSI_CACHE_SIZE": "1000000000",
    "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": ".tif,.tiff",
    "CPL_VSIL_CURL_USE_HEAD": "NO",
    "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",
    "TITILER_API_CACHE_SIZE": "1024",
}

for key, value in DEFAULT_ENV.items():
    os.environ.setdefault(key, value)

# -----------------------------
# App-level settings
# -----------------------------
CORS_ALLOW_ORIGINS = ["*"]
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

# -----------------------------
# Gunicorn (optional reference)
# -----------------------------
GUNICORN_WORKERS = int(os.getenv("GUNICORN_WORKERS", "4"))
GUNICORN_TIMEOUT = int(os.getenv("GUNICORN_TIMEOUT", "120"))

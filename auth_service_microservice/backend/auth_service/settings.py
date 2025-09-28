# settings.py
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
DEBUG = 'RENDER' not in os.environ  # Render setea variables por defecto

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
RENDER_HOST = os.getenv("RENDER_EXTERNAL_HOSTNAME")  # la define Render
if RENDER_HOST:
    ALLOWED_HOSTS.append(RENDER_HOST)

# CORS/CSRF para el frontend
FRONTEND_URL = os.getenv("FRONTEND_URL")
CSRF_TRUSTED_ORIGINS = []
if RENDER_HOST:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_HOST}")
if FRONTEND_URL:
    # Acepta tu sitio de frontend
    CSRF_TRUSTED_ORIGINS.append(FRONTEND_URL)
CORS_ALLOWED_ORIGINS = [FRONTEND_URL] if FRONTEND_URL else []
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    # ...
    "corsheaders",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # ...
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
    )
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

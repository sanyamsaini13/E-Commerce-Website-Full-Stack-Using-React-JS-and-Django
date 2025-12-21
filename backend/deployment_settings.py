import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR


RENDER_HOST = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

ALLOWED_HOSTS = [RENDER_HOST] if RENDER_HOST else ["localhost", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = (
    [f"https://{RENDER_HOST}"] if RENDER_HOST else []
)

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key-for-local")


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",   # after security
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# CORS (use ONE of these)


CORS_ALLOWED_ORIGINS = ["https://e-commerce-web-full-stack-frontend.onrender.com"]


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
    )
}



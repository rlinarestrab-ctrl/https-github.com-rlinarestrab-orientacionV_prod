#!/usr/bin/env bash
set -e

# Migraciones (usa DATABASE_URL de Render/Neon)
python manage.py migrate --noinput

# Por si agregaste nuevos assets
python manage.py collectstatic --noinput

# Ejecuta gunicorn con el módulo WSGI que definiremos por env var
# Ej: DJANGO_WSGI_MODULE=auth_project.wsgi
gunicorn ${DJANGO_WSGI_MODULE}:application --bind 0.0.0.0:8000 --workers 3 --timeout 120

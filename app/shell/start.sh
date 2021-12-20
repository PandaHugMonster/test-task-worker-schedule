#!/usr/bin/env bash

cd /app;

_IP="0.0.0.0";
_PORT="8005";
_USER="root";
_PASS="root";
_EMAIL="test@test.test";

wait-for-it --service db:5432 --timeout 0 -- ./manage.py migrate;

DJANGO_SUPERUSER_PASSWORD="${_PASS}" \
DJANGO_SUPERUSER_EMAIL="${_EMAIL}" \
./manage.py createsuperuser --username "${_USER}" --noinput


./manage.py runserver "${_IP}:${_PORT}";

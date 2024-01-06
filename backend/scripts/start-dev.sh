#!/usr/bin/env bash

set -e

# python manage.py runserver
uvicorn app.asgi:application --reload
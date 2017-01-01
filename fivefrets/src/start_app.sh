#!/bin/bash

sleep 10
su -m ffrets -c "python3 manage.py makemigrations"
su -m ffrets -c "python3 manage.py migrate"
su -m ffrets -c "python3 manage.py collectstatic --noinput"
# su -m ffrets -c "python3 manage.py runserver 0.0.0.0:8000"
su -m ffrets -c "gunicorn fivefrets.wsgi:application -w 2 -b :8000"

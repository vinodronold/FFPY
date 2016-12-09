#!/bin/bash

sleep 10
su -m ffrets -c "python3 manage.py makemigrations"
su -m ffrets -c "python3 manage.py migrate"
su -m ffrets -c "python3 manage.py runserver 0.0.0.0:8000"

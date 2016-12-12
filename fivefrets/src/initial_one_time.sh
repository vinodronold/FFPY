#!/bin/bash

echo 'One Time Initial Setup Script . . .'

python3 manage.py createsuperuser

python3 manage.py loaddata chords/data.json

locale-gen en_US en_US.UTF-8

echo 'select 149 for UTF-8 and select 3 for en.UTF-8'

dpkg-reconfigure locales

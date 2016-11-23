#!/bin/bash

echo 'One Time Initial Setup Script . . .'

python manage.py createsuperuser

python manage.py loaddata chords.chordModel.json

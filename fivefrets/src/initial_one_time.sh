#!/bin/bash

echo 'One Time Initial Setup Script . . .'

python3 manage.py createsuperuser

python3 manage.py loaddata chords.chordModel.json

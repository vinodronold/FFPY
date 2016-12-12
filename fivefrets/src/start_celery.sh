#!/bin/bash

sleep 120

# celery worker -A fivefrets.celeryconf -Q default -n default@%h
su -m ffrets -c "celery -A fivefrets worker -l info"

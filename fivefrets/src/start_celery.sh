#!/bin/bash

sleep 180

# celery worker -A fivefrets.celeryconf -Q default -n default@%h
celery -A fivefrets worker -l info

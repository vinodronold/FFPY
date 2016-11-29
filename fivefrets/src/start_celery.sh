#!/bin/bash

sleep 10

celery worker -A fivefrets.celery -Q default -n default@%h

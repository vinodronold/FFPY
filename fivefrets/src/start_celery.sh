#!/bin/bash

sleep 10

celery worker -A fivefrets.celeryconf -Q default -n default@%h

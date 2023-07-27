#!/bin/sh



python /crypto/manage.py makemigrations
python /crypto/manage.py migrate
python /crypto/manage.py runserver 0.0.0.0:8000

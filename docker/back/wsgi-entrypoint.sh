#!/bin/sh

exec gunicorn --bind 0.0.0.0:5000 --workers 2 app:create_app

#!/bin/bash

/root/.poetry/bin/poetry run python manage.py migrate
tail -f /opt/app/logs/$(date +"%Y_%m_%d")_events.log
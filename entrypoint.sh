#!/bin/bash

/root/.poetry/bin/poetry run python manage.py migrate
tail -f /dev/null
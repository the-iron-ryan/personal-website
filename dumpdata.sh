#!/usr/bin/env bash

python manage.py dumpdata --exclude=auth --exclude=sessions \
--indent 2 > db.json
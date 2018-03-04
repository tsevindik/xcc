#!/bin/sh
python /app/manage.py collectstatic --noinput
echo "###########################3"
echo $(`pwd`)
echo $(`ls`)
echo "###########################3"
/usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app
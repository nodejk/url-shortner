#!/usr/bin/env bash

set -e

DEFAULT_MODULE_NAME=app.main

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-info}
LOG_CONFIG=${LOG_CONFIG:-/src/logging.ini}

if [[ $ENVIRONMENT = "DEV" ]]; then
    exec uvicorn --reload --proxy-headers --host $HOST --port $PORT "$APP_MODULE";
else
    exec /usr/local/bin/gunicorn "$APP_MODULE" -w 4 -k uvicorn.workers.UvicornWorker;
fi

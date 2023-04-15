#!/bin/bash
source venv/bin/activate
export FLASK_APP=wsgi.py
export FLASK_DEBUG=true
flask run --port 8000

deactivate

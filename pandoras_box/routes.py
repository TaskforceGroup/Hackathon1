from flask import render_template

from . import app

# Import the database accessors
from .db_services import *


@app.route('/')
def root():
    return render_template('timeline.html')


# These are temporary URL endpoints to run functions

@app.route('/This_is_another_route')
def temp_sms_import():
    """
    This is an example
    """
    result = 'a'
    return f'This is the import result: <br><br>{result}'

@app.route('/api/groups')
def groups():
    return get_groups()


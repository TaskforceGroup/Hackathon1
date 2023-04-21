# Import the python packages
from flask import render_template

# Import the 
from . import app

# Import the database accessors
from . import db_services as db


@app.route('/')
def root():
    return render_template('timeline.html')


# --- --- --- The API --- --- ---

@app.route('/api/groups')
def get_groups():
    return db.get_groups()


@app.route('/api/new_group', methods=['GET', 'POST'])
def new_group():
    name = request.args.get('name')
    description = request.args.get('description')
    db.new_group(name, description)
    # Return all groups now that the new one has been added
    return db.get_groups()


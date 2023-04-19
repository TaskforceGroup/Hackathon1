from flask import render_template, jsonify

from . import app


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
    json_data = {
        'groups': [
            {'name': 'Group A', 'description': 'Dedicated to finding Nick guilty', 'data': [
                'look at stars', 'Eat donuts', 'Play LOL'
                ]
            },
            {'name': 'Group B with a longer name', 'description': 'Free food events', 'data': [
                'Going to Walmart', 'Went to gym', 'look at rocks'
                ]
            }
        ]
    }
return jsonify(json_data)


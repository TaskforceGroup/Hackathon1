from . import app


@app.route('/')
def root():
    return 'Welcome to the app. There is no user interface yet. <br><br><br>Goodbye'


# These are temporary URL endpoints to run functions

@app.route('/This_is_another_route')
def temp_sms_import():
    """
    This is an example
    """
    result = 'a'
    return f'This is the import result: <br><br>{result}'

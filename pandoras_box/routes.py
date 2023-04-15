from app import app, importers


@app.route('/')
def root():
    return 'Welcome to the app. There is no user interface yet. <br><br><br>Goodbye'


# These are temporary URL endpoints to run functions



@app.route('/import_sms')
def temp_sms_import():
    """
    This is for testing the import function.
    Unformatted data will be returned to the html page
    """
    result = 'a'
    return f'This is the import result: <br><br>{result}'

venv\Scripts\Activate.ps1
pip install -r requirements.txt

$env:FLASK_APP = 'wsgi.py' # Tell the local computer where to start
$env:FLASK_DEBUG = 'true' # Enable debug messages

flask run --port 8000

deactivate # exit the Python environment

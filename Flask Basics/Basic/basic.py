# create Virtual environmrnt: cirtualenv <environment name>
# active Virtual environment: env/Scripts/active.bat
# Intall: pip install Flask
# __pycache__ folder alway created for stop this use 
# '$env:PYTHONDONTWRITEBYTECODE=1'
# run this command and this file creation stops

# run application: flask --app <file name>.py --debug run

# path name and function name must different

# ----------------------------------------------------------------------------

# Topic:  Basic Structure for the flask api
from flask import Flask

# part-1
# WSGI application create for Communication
app = Flask('__name__')

# part-2
# decorator: @app.route('<URL>')
@app.route('/')
def working():
    return "I'm Prince malani, and this is my First API."

@app.route('/decorator')
def decorator():
    return {'data': "Welcome to Decorator."}

@app.route('/members')
def members():
    return 'There Are many people who work hear'

from markupsafe import escape

# prince the name
@app.route('/<name>')
def Hello(name):
    return f"Hello, {name}"

# part-3 
# when this function called at that time, function start running 
if __name__ == '__main__':
    app.run(debug=True)
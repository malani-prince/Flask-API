# create Virtual environmrnt: cirtualenv env
# active Virtual environment: env/Scripts/active.bat

# Basic Structure for the flask api

# run application: flask --app <file name>.py --debug run

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



# part-3 
# when this function called at that time, function start running 
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
# part-1
# WSGI application create for Communication
app = Flask('__name__')

# part-2
# decorator: @app.route('<URL>')
@app.route('/')
def working():
    return "I'm Prince malani, and this is my First API."

# rule : do not fill the spacae between 
# <int:{variable name}>        [✔️]
# <int: {variable name}>       [❌]

@app.route('/success_rate/<int:success>')
def success(success):
    if success  <= 100:
        return {
            'success rate': success,
            'fail rate': 100- success
        }
    else:
        return 'Try Again'

@app.route('/fail_rate/<int:fail>')
def fail(fail):
    if fail <=100 :
        return {
            'success rate': 100 - fail,
            'fail rate': fail
        }
    else:
        return "Try Again"

@app.route('/allow/<int:Number>')
def allow(Number):
    if Number < 18:
        return f'You have been allowed to enter because your number is {str(Number)}'
    else:
       return f'You are not allowed'

# part-3 
# when this function called at that time, function start running 
if __name__ == '__main__':
    app.run(debug=True)
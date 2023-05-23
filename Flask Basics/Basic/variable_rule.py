from flask import Flask

app = Flask(__name__)

# integer object
@app.route('/int_value_pass/<int:number>')
def number_pass(number):
    return {'number': number}

# string object
@app.route('/string_value_pass/<name>')
def string_pass(name):
    return {'number': name}

# string object
@app.route('/float_value_pass/float:<val>')
def float_pass(val):
    return {'number': val}
    
if __name__ == '__main__':
    app.run(debug=True)
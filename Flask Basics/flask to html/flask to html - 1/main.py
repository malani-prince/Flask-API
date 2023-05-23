# Integrate HTML With Flask
# HTTT verb: GET and POST

# rules 
# in redirect: in the redirect we name should be different fot the path and funtion
# for redirect, pass function into the ('<function name >', <parameter of callable function> = <assigned value>)


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# store the result of the students and disply using function
@app.route('/')
def welcome():
    return render_template('index.html')
    
@app.route('/pass/<int:val>')
def passing_marks(val):    
    return f"student pass: {str(val)} marks"

@app.route('/pass/<int:val>')
def fail_marks(val): 
    return f"student fail: {str(val)} marks"

@app.route('/marks/<int:number>')
def insert_number(number):
    if number >= 60:
        return redirect(url_for('passing_marks', val = number))
    else:
        return redirect(url_for('fail_marks', val = number))

# --------------------------------------------------------------------------------
# Fatch the data from html from and redirect to the unother page dynamic

@app.route('/success/<int:val>')
def Success_score(val):
    res=''
    if val >= 50:
        res = 'pass'
    else:
        res = 'fail'
    return render_template('results.html', results = res, marks = val )

@app.route('/submit_marks', methods=['POST', 'GET'])
def submit_marks():
    total_score = 0 
    if request.method == 'POST':
        maths =float(request.form['maths'])
        ds =float(request.form['DataScience'])
        flask =float(request.form['Flask'])
        python =float(request.form['python'])
        django =float(request.form['Django'])
        total_score = (maths+ds+flask+python+django)/5
    return redirect(url_for("Success_score", val = total_score))
         

if __name__ == '__main__':
    app.run(debug=True)
    

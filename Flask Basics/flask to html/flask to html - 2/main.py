# Integrate HTML With Flask
# HTTT verb: GET and POST

# rules 
# in redirect: in the redirect we name should be different fot the path and funtion
# for redirect, pass function into the ('<function name >', <parameter of callable function> = <assigned value>)

# lecture-4

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# store the result of the students and disply using function
# @app.route('/')
# def welcome():
#     return render_template('index2.html')
    
# @app.route('/pass/<int:val>')
# def passing_marks(val):    
#     return f"student pass: {str(val)} marks"

# @app.route('/pass/<int:val>')
# def fail_marks(val): 
#     return f"student fail: {str(val)} marks"

# @app.route('/marks/<int:number>')
# def insert_number(number):
#     if number >= 60:
#         return redirect(url_for('passing_marks', val = number))
#     else:
#         return redirect(url_for('fail_marks', val = number))

# --------------------------------------------------------------------------------
# lecture-5
# Fatch the data from html from and redirect to the unother page dynamic

# @app.route('/success/<int:val>')
# def Success_score(val):
#     res=''
#     if val >= 50:
#         res = 'pass'
#     else:
#         res = 'fail'
#     return render_template('results.html', results = res, marks = val )

# @app.route('/submit_marks', methods=['POST', 'GET'])
# def submit_marks():
#     total_score = 0 
#     if request.method == 'POST':
#         maths =float(str(request.form['maths'])),
#         ds =float(str(request.form['DataScience'])),
#         flask =float(str(request.form['Flask'])),
#         python =float(str(request.form['python'])),
#         django =float(str(request.form['Django'])),
#         total_score = (maths+ds+flask+python+django)/5
#     return redirect(url_for("Success_score", val = total_score))
         
#--------------------------------------------------------------------------------------------111-
# lecture-6: jinja2 template engine

'''
{%...%}: condition
{{   }}: expression print
{#...#}: comments in page
'''

# @app.route('/')
# def welcome():
#     return render_template('index.html')


# @app.route('/success/<int:val>')
# def Success_score(val):
#     return render_template('results.html', marks = val )

# @app.route('/submit_marks', methods=['POST', 'GET'])
# def submit_marks():
#     total_score = 0 
#     if request.method == 'POST':
#         maths =float(request.form['maths'])
#         ds =float(request.form['DataScience'])
#         flask =float(request.form['Flask'])
#         python =float(request.form['python'])
#         django =float(request.form['Django'])
#         total_score = (maths+ds+flask+python+django)/5
#     return redirect(url_for("Success_score", val = total_score))
         
# make a View for the Employee details:

@app.route('/')
def welcome_employee():
    return render_template('employee_index.html')
    
@app.route('/Employee_Details', methods=['POST', 'GET'])
def insert_details():
    employee_data = {}
    if request.method == 'POST':
        employee_data={
            "name": str(request.form['name']),
            # "dob": str(request.form['date_of_birth']),
            "gender": str(request.form['gender']),
            "job_title": str(request.form['job_title']),
            "department": str(request.form['department']),
            "mail": str(request.form['work_email_address']),
            # "start_date": str(request.form['start_date']),
            "salary": float(request.form['salary'])
        }
    return render_template('employee_results.html', DATA =  employee_data)

if __name__ == '__main__':
    app.run(debug=True)
    

# Integrate HTML With Flask
# HTTT verb: GET and POST

# rules 
# in redirect: in the redirect we name should be different fot the path and funtion
# for redirect, pass function into the ('<function name >', <parameter of callable function> = <assigned value>)

# lecture-4

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

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
    

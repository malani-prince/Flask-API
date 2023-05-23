# rules 
# in redirect: in the redirect we name should be different fot the path and funtion
# for redirect, pass function into the ('<function name >', <parameter of callable function> = <assigned value>)

from flask import Flask, redirect, url_for

app = Flask(__name__)

python = {'marks': [], 'student_name': []}
cpp = {'marks': [], 'student_name': []}
maths = {'marks': [], 'student_name': []}
django = {'marks': [], 'student_name': []}
ml = {'marks': [], 'student_name': []}
ai = {'marks': [], 'student_name': []}

# store the result of the students and disply using function
@app.route('/')
def Aim():
    return {
        "Aim": "This APi have functionality to enter marks and store inot the list or dictionary",
        "Route_availabele": {
            "python": '/python_marks',
            "cpp": '/cpp_marks',
            "maths": '/maths_marks',
            "django": '/django_marks',
            "ml": '/ml_marks',
            "ai": '/ai_marks'
        }
    }
    
@app.route('/python_marks/<int:Number>/<string:Name>')
def Python_insert(Number, Name):
    python['marks'].append(Number)
    python['student_name'].append(Name)
    return python
    
@app.route('/cpp_marks/<int:Number>/<string:Name>')
def cpp_insert(Number, Name):
    cpp['marks'].append(Number)
    cpp['student_name'].append(Name)
    return cpp
    
@app.route('/ai_marks/<int:Number>/<string:Name>')
def ai_insert(Number, Name):
    ai['marks'].append(Number)
    ai['student_name'].append(Name)
    return ai

@app.route('/maths_marks/<int:Number>/<string:Name>')
def maths_insert(Number, Name):
    maths['marks'].append(Number)
    maths['student_name'].append(Name)
    return maths
    
@app.route('/django_marks/<int:Number>/<string:Name>')
def django_insert(Number, Name):
    django['marks'].append(Number)
    django['student_name'].append(Name)
    return django
    
@app.route('/ml_marks/<int:Number>/<string:Name>')
def ml_insert(Number, Name):
    ml['marks'].append(Number)
    ml['student_name'].append(Name)
    return ml

@app.route('/get_result')
def show():
    return {
        'python': python,
        'cpp': cpp,
        'ai': ai,
        'ml': ml,
        'maths': maths,
        'django': django
    }

@app.route('/pass/<int:m>')
def pass_student(m):
    return f"Student Pass SuceessFully with good marks {str(m)}"

@app.route('/pass_fail/<int:marks>')
def pass_fail_student(marks):
    if marks > 60:
        return redirect(url_for('pass_student',m =  marks))
    else:
        return 'fail'

if __name__ == '__main__':
    app.run(debug=True)
    

# play with the multiple files using app
# use controller model architecture
# if we declare "from controller import *" above then it can't render the page 
# run this command before the start programming 
# $env:PYTHONDONTWRITEBYTECODE=1  
# install mysql
# install PyJWT

from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
app = Flask(__name__)
import jwt

# from controller import user_controler, product_controller
# we want to add the file name manually insted of that we are going to import whole directory
from controller import *

# -----------------------------------------------------------------------------------------------------
#                                      CRUD Operation using Flask API
# -----------------------------------------------------------------------------------------------------

@app.route('/')
def welcome():
    return "Welcome to API"

@app.route('/users')
def user_route():
    return render_template('index_employee.html')

@app.route('/update')
def update_user():
    return render_template('take_id.html')

@app.route('/delete')
def Delete_user():
    return render_template('delete_user.html')

# -----------------------------------------------------------------------------------------------------
#                                      make_response methos & HTTP Response Codes
# -----------------------------------------------------------------------------------------------------

@app.route('/make_response')
def make_response_try():
    return redirect(url_for('try_make_response'))

@app.route('/page/<start>/<limit>')
def pagination_data(start, limit):
    return redirect(url_for('fetch_data_controller', start = start, limit=limit))

# -----------------------------------------------------------------------------------------------------
#                                               File Uploading
# -----------------------------------------------------------------------------------------------------

# Problem:
# 1) uploading file postman to server
# 2) unique file name
# 3) updating filepath in database with respective entity
# 4) creating end point to read the file

# put = upload file and save into database
# Reference controller.

# -----------------------------------------------------------------------------------------------------
#                                               Project-1: TODO LIST
# -----------------------------------------------------------------------------------------------------
from models.todo_model import todo_model
from functools import wraps
obj = todo_model()

# def token_require(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = request.headers.get('token')
        
        if not token:
            return {
                "message": "enter valid token...!"
            }
        try:
            decode_token = jwt.decode(
                token,
                key =obj.secratekey,
                algorithms="HS256"
            )
        except:
            return {
                "message": "enter valid token....!"
            }
            
        return f(decode_token ,*args, **kwargs)

    return decorated

@app.route('/todo')
def todo():
    return "all user are hear"

@app.route('/todo/all_user', methods=['GET'])
@token_required
def get_all_user(decode_token): 
    
    if decode_token['payload'][0]['admin'] == 0:
        return {
            "message": "promotaion require"
        }
        
    connector = obj.return_con()
    cursor = connector.cursor(dictionary=True)
    
    query = "SELECT * FROM todo.user"
    cursor.execute(query)
    data = cursor.fetchall() 
    
    total_id = obj.return_total_public_id()
    return {
        # "Decode Token Data": token,
        "data": data
    }

@app.route('/todo/get_user/<public_id>', methods=['GET'])
def get_one_user(public_id):
    total_public_id =obj.return_total_public_id()
    
    if public_id in total_public_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)
        query = f"SELECT * FROM todo.user where public_id='{public_id}';"
        cursor.execute(query)
        data = cursor.fetchall()
        return {
            "total":data
        }
    else:
        return "not valid id valid id"
    

@app.route('/todo/post_user', methods=['POST'])
def post_public_id():
    data = dict(request.form)
    connector = obj.return_con()
    cursor = connector.cursor(dictionary=True)
    
    query = f"INSERT INTO todo.user (public_id, name, pass, admin) VALUES ('{data['public_id']}', '{data['name']}','{data['pass']}' ,'{data['admin']}');"
    cursor.execute(query)
    return {
        "meg": "Data insert into DataBase successfully..!"
    }

@app.route('/todo/put_user/<public_id>', methods=['PUT'])
def put_public_id(token ,public_id):
    if token['payload'][0]['admin'] == 0:
        return {      
                "message": "promotaion require"
        }
        
    total_public_id =obj.return_total_public_id()
          
    if public_id in total_public_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)

        query = f"UPDATE todo.user SET admin = {'1'} WHERE (public_id = '{public_id}');"
        cursor.execute(query)
        return {
            "public id": public_id,
            "role": "Admin"
        }
    else:
        return "enter valid public id"

@app.route('/todo/delete_user/<id>', methods=['DELETE'])
def detele_public_id( id):
    x = int(id)
    total_id = obj.return_total_id()
    if x in total_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)
        total_id = obj.return_total_id()
        
        query = f"DELETE FROM todo.user WHERE id= {id}"
        cursor.execute(query)
        data = cursor.fetchall() 
        return {
           "message": "user Deleted successfully.......!!"
        }
    else:
        return "enter valid id"

@app.route('/todo/login')
def user_login():
    
    total_id = obj.return_total_id()
    auth = request.authorization
    
    if not auth:
        return "enter usernmae and passwords.....!!"
    
    if int(auth['username']) in total_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)
        query = f"SELECT pass from todo.user where id={int(auth['username'])};"
        cursor.execute(query)
        data = cursor.fetchone()
        
        if data['pass'] == auth['password']:
            # Epoch Time Runs:
            time = datetime.now() + timedelta(minutes=30)
            epoch_time = int(time.timestamp())
            
            # fetch employee information 
            connector = obj.return_con()
            cursor = connector.cursor(dictionary=True)
            query = f"select id, admin from todo.user WHERE id = {auth['username']} ;"
            cursor.execute(query)
            emp_data = cursor.fetchall() 
            # create the pyload which pass through, Encode function, with exparation time
            payload = {
                'payload': emp_data,
                # 'exp': epoch_time,
            }
            # key  = Secrate key, use for pretect the secrate message.
            jtoken = jwt.encode(
                payload, 
                key = obj.secratekey
            )
            return make_response({
                "data": auth,
                "token": jtoken,
            }, 200)
        else:
            return {
                "message": "enter valid password"
            }
    else:
        return {
            "message": "invalid user........!!"
        }

@app.route('/todo/get_all_list', methods=['GET'])
@token_required
def get_all_todo_list(decode_token):
    if decode_token['payload'][0]['admin'] == 0:
        return {
            "message": "promotaion require"
        }
    
    connector = obj.return_con()
    cursor = connector.cursor(dictionary=True)
    query = f"SELECT * FROM todo.todo;"
    cursor.execute(query)
    todo_data = cursor.fetchall() 
    
    # total_id = obj.return_total_id_of_todo_data()
    
    return {
        # "total_id": total_id,
        "decode token": decode_token,
        "todo_data": todo_data
    }

#--------------------------------------------------------------------

@app.route('/todo/get_one_list/<todo_id>', methods=['GET'])
def get_one_todo_list_using_id(todo_id):
    total_id = obj.return_total_id_of_todo_data()
    todo_id = int(todo_id)
    if todo_id in total_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)
        query = f"select * from todo.todo where id={todo_id};"
        cursor.execute(query)
        data = cursor.fetchall()
        return {
            "data": data
        }
    else:
        return {
            "message": "enter valid data......!"
        }
        
#--------------------------------------------------------------------
    
@app.route('/todo/add_new_list', methods=['POST'])
def add_new_list():
    data = request.form
    if not data:
        return {
            "message": "enter valid data"
        }
    
    connector = obj.return_con()
    cursor = connector.cursor(dictionary=True)
    query = f"INSERT INTO todo.todo (text, compelete) VALUES ('{data['text']}', '{data['compelete']}');"
    cursor.execute(query)
    return {
        "data": "Data Insert SuccessFully.......!",
        "inserted Data": data
    }

#-----------------------------------------------------------------------

@app.route('/todo/update_list/<task_completion_id>', methods=['PUT'])
def put_todo_list(task_completion_id):
    total_id = obj.return_total_id_of_todo_data()
    task_completion_id = int(task_completion_id)
    
    if task_completion_id in total_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)
        query = f"Update todo.todo set compelete='1' where id={task_completion_id}"
        cursor.execute(query)
        data = cursor.fetchall()
        return {
            "message": "Todo List Updated Successfully"
        }
    else:
        return {
            "message": "enter valid id......!"
        }

#-----------------------------------------------------------------------

@app.route('/todo/delete_tdo_list/<todo_id>',methods=['DELETE'])
def delete_todo_list(todo_id):    
    total_id = obj.return_total_id_of_todo_data()
    todo_id = int(todo_id)
    
    if todo_id in total_id:
        connector = obj.return_con()
        cursor = connector.cursor(dictionary=True)
        query = f"DELETE from todo.todo where id={todo_id};"
        cursor.execute(query)
        data = cursor.fetchall()
        return {
            "message": "Todo List Deleted"
        }

    else:
        return {
            "message": "enter valid data......!"
        }
        
#-----------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
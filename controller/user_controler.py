from app import app
from models.user_model import user_model

from flask import request, render_template, jsonify, make_response, send_file
from datetime import datetime, date, time, timedelta
from functools import wraps
import jwt
# -----------------------------------------------------------------------------------------------------
#                                      CRUD Operation using Flask API
# -----------------------------------------------------------------------------------------------------

# show all user
obj = user_model()

@app.route('/users/get_all')
def user_getall_controller():
    return obj.user_get_all_model()
    
# add new user
obj = user_model()
@app.route('/users/add_new_user', methods = ['POST', 'GET'])
def add_new_user_controller():
    if request.method == 'POST':
        return obj.user_add_new_user(dict(request.form))
    else:
        return render_template('error_msg_for_insert_data.html')

# update User
@app.route('/update/get_id', methods=['POST'])
def update_details():
    data = int(request.form['id'])
    
    con = obj.return_con()
    cursor = con.cursor(dictionary=True)
    
    query = "SELECT id FROM flask_api.users;"
    
    cursor.execute(query)
    total_id = cursor.fetchall()
    
    t1 = [total_id[i]['id'] for i in range(len(total_id))]
    
    # print(total_id)
    if data in t1:
        return obj.Take_id_from_user(data)
    else:
        return render_template('ID_ERROR.html')
    

@app.route('/update/final_changes', methods=['POST'])
def change_DB():
    if request.method == 'POST':
        return obj.changes_reflect_on_DB(dict(request.form))

# delete User
@app.route('/delete/delete_id',methods=['POST'])
def find_id_for_delete_operation():
    if request.method == 'POST':
        did = {"delete_id" :int(request.form['deleteid'])}

        con = obj.return_con()
        cursor = con.cursor(dictionary=True)
        
        query = "SELECT id FROM flask_api.users;"
        
        cursor.execute(query)
        total_id = cursor.fetchall()
        
        t1 = [total_id[i]['id'] for i in range(len(total_id))]
        
        # print(total_id)
        x = int(did['delete_id'])
        
        if x in t1:
            return obj.delete_from_DB(did)
        else:
            return render_template('ID_ERROR.html')
    else:
        return render_template('error_msg_for_insert_data.html')
    
# -----------------------------------------------------------------------------------------------------
#                                      Make Reaponse & HTTP response
# -----------------------------------------------------------------------------------------------------

@app.route('/make_response/try')
def try_make_response():
    return render_template('make_respomse.html')

# -----------------------------------------------------------------------------------------------------
#          Update only Perticular Attribute like name only, mail only, some time mail and name both 
# -----------------------------------------------------------------------------------------------------

def return_connection_and_cursor_object():
    connect = obj.return_con()
    cursor = connect.cursor(dictionary=True)
    return cursor

def return_total_id():
    con = obj.return_con()
    cursor = con.cursor(dictionary=True)    
    query = "SELECT id FROM flask_api.users;"
        
    cursor.execute(query)
    total_id = cursor.fetchall()    
    
    t1 = [total_id[i]['id'] for i in range(len(total_id))]
        
        # print(total_id)
    return t1

# pagination data hear called with start and limit value 
@app.route('/data/<start>/<limit>')
def fetch_data_controller(start, limit):
    
    return obj.petch_data_methods(start, limit)
    # return {
    #     "use": [start, limit]
    # }

@app.route('/fileupload/<uid>/upload/avatar', methods=['PUT'])
def file_upload_avatar_controller(uid):
    # Fatch the file using .files methos
    # avatar is file name 
    file = request.files['avatar']
    unique_file_name = str(datetime.now().timestamp()).replace(".","")
    split_name = file.filename.split(".")
    extension = split_name[1]
    path = f"uploads/{split_name[0]}{unique_file_name}.{extension}"
    file.save(path)
    print(uid)
    return obj.file_upload_avatar_models(path, uid)

#fetch the file using Postman API
@app.route('/uploads/<filename>')
def user_get_avatar_controller(filename):
    try:
        return send_file(f"uploads/{filename}")
    except Exception as e:
        return e
    
# JWT token Return 

# return the token
@app.route('/user/login', methods= ['POST'])
def user_login_controller():
    data = request.form
    return  obj.user_login_model(data)

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
        
#         if not token:
#             return jsonify({"message" :"enter valid token"})
#         try:
#             data = jwt.decode(token, obj.secratekey)
#         except:
#             return jsonify({"message": "Token invalid"})
        
#         return f(*args, **kwargs)
#     return decorated

@app.route('/unprotected')
def unprotected():
    return ''

@app.route('/protected')
# @token_required
@obj.token_required
def protected():
    return 'This is only with the availble use'



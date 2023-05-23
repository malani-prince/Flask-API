import mysql.connector
import json
from flask import render_template, redirect, url_for, make_response, request, jsonify
from datetime import datetime, date, time, timedelta
import jwt
from functools import wraps
# -----------------------------------------------------------------------------------------------------
#                                      CRUD Operation using Flask API
# -----------------------------------------------------------------------------------------------------

class user_model():
    def __init__(self):
        self.id = 0
        self.total_id = []
        self.secratekey = "asdflkjhmnbvzxcpqowieuryt"
        # connection between mysql and python
        try:
            self.con = mysql.connector.connect(
                user = 'Prince Malani',
                password = 'Hetu@0617',
                database = 'flask_api'
                )
            # cursor object
            self.con.autocommit = True
            self.cursor = self.con.cursor(dictionary=True)
            print('Done-Connection')
        except Exception as e:
            print(e)
    
    def return_con(self):
        return self.con
    
    def return_total_id(self):
        query = "SELECT id FROM flask_api.users;"
        self.cursor.execute(query)
        self.total_id = self.cursor.fetchall()
        t1 = [self.total_id[i]['id'] for i in range(len(self.total_id))]
        return t1
    
    def user_get_all_model(self):
        self.cursor.execute("select * from users")
        results = self.cursor.fetchall()
        if len(results) >=1:
            return results
        else:
            return {"msg": "Data not found"}

    def user_add_new_user(self, data):
        query = f"insert into flask_api.users (fname, lname, mail, city, role, phone, salary) values ('{data['first_name']}', '{data['last_name']}', '{data['mail_address']}', '{data['city']}', '{data['role']}', {data['phone_number']}, '{data['salary']}'); "
        self.cursor.execute(query)
        return {
            "": "New row inserted.",
            "url to see the data": '/users/get_all',
            "enter Data": data
        }
    
    def Take_id_from_user(self, id):
        query = f"select * from flask_api.users where id={id}"
        self.cursor.execute(query)
        x = self.cursor.fetchone()
        self.id = id
        return render_template('update_employee.html', data = x)
    
    def changes_reflect_on_DB(self, data):
        # update
        try:
            query = f"UPDATE flask_api.users SET fname = '{data['first_name']}', lname = '{data['last_name']}', mail = '{data['mail_address']}', city = '{data['city']}', role = '{data['role']}', phone = '{data['phone_number']}', salary = '{data['salary']}' WHERE (id = {self.id});"
            self.cursor.execute(query)
            return {
                "MSG": "Update Successfull",
                "id": self.id,
                "Update-data": data
            }
        except Exception as e:
            return e
        
    def delete_from_DB(self, did):
        try:
            # fetch total number of ID
            query = "SELECT id FROM flask_api.users;"
            self.cursor.execute(query)
            self.total_id = self.cursor.fetchall()
            t1 = [self.total_id[i]['id'] for i in range(len(self.total_id))]
            
            query3 = f"SELECT * FROM flask_api.users where id={did['delete_id']};"
            self.cursor.execute(query3)
            previous_data = self.cursor.fetchone()
            
            query2 = f"DELETE FROM flask_api.users WHERE (id = {did['delete_id']});"
            self.cursor.execute(query2)
            
            # print(total_id)
            x = int(did['delete_id'])
            if x in t1:
                return {
                    "Delete id": did['delete_id'],
                    "msg": "Delete successfully",
                    "Previous data": previous_data,
                    "varify": "/users/get_all",
                }
            else:
                return render_template('ID_ERROR.html')
        
        except Exception as e:
            return e
                
    # -----------------------------------------------------------------------------------------------------
        
    def petch_data_methods(self, start, limit):
        limit = int(limit)
        start = int(start)
        start = int((limit*start)-limit)
        query = f"SELECT * FROM flask_api.users LIMIT {(start)}, {limit};"
        self.cursor.execute(query)
        emp_data = self.cursor.fetchall()
        # return {
        #     "start": start,
        #     "limit": limit,
        #     "emp data": emp_data
        # }
        return render_template('details.html', empdata = emp_data)

    def file_upload_avatar_models(self, path, id):
        id = int(id)
        path = f"/{path}"
        query = f"UPDATE flask_api.users SET avatar = '{path}' WHERE (id = {id});"
        self.cursor.execute(query)
        return make_response("update success fully", 200)

    # JWT  Token return 

    def user_login_model(self, data):    
        total_id = self.return_total_id()
    
        query = f"SELECT id, pass FROM flask_api.users where id= {int(data['id'])};"
        self.cursor.execute(query)
        emp_data = self.cursor.fetchone()
            
        if (int(data['id']) in total_id) and (emp_data['pass'] == data['pass']):
            query2 = f"SELECT id, fname, lname, mail, city, role, phone, salary, avatar, role_id FROM flask_api.users where id={int(data['id'])}"    
            self.cursor.execute(query2)
            perticular_emp = self.cursor.fetchone()
            
            time = datetime.now() + timedelta(minutes=30)
            epoch_time = int(time.timestamp())
            
            payload = {
                'payload': emp_data,
                'exp': epoch_time,
                'data': perticular_emp
            }
            # key  = Secrate key which use for pretect the secrate key.
            jtoken = jwt.encode(
                payload, 
                key = self.secratekey,
                algorithm="HS256")
            
            return make_response({
                "token": jtoken,
            }, 200)
        else:
            return "Enter valid ID or password"
        
    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.args.get('token')
            if not token:
                return jsonify({"message" :"Missing Token"})
            try:
                data = jwt.decode(token, self.secratekey, algorithms="HS256")
                return {
                    "data": data
                }
            except:
                return {"message": "enter valid token"}
            return f(*args, **kwargs)
        return decorated

import mysql.connector
import json
from flask import render_template, redirect, url_for, make_response, request, jsonify
from datetime import datetime, date, time, timedelta
import jwt
from functools import wraps
# -----------------------------------------------------------------------------------------------------
#                                      CRUD Operation using Flask API
# -----------------------------------------------------------------------------------------------------

class todo_model():
    def __init__(self):
        self.id = 0
        self.total_id = []
        self.total_public_key = []
        self.secratekey = "asdflkjhmnbvzxcpqowieuryt"
        # connection between mysql and python
        try:
            self.con = mysql.connector.connect(
                user = 'Prince Malani',
                password = 'Hetu@0617',
                database = 'todo'
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
        query = "SELECT id FROM todo.user;"
        self.cursor.execute(query)
        self.total_id = self.cursor.fetchall()
        t1 = [self.total_id[i]['id'] for i in range(len(self.total_id))]
        return t1
    
    def return_total_public_id(self):
        query = "SELECT public_id FROM todo.user;"
        self.cursor.execute(query)
        self.total_public_key = self.cursor.fetchall()
        t1 = [self.total_public_key[i]['public_id'] for i in range(len(self.total_public_key))]
        return t1
    
    def return_total_id_of_todo_data(self):
        query = "SELECT id FROM todo.todo;"
        self.cursor.execute(query)
        self.total_id = self.cursor.fetchall()
        t1 = [self.total_id[i]['id'] for i in range(len(self.total_id))]
        return t1
#app.py
from flask import Flask, jsonify, request, session
import psycopg2
app = Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    _json=request.json
    _username=_json['username']
    _password=_json['password']
    connection = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")
    cursor = connection.cursor()
    sql = "SELECT * FROM register WHERE first_name=%s and password=%s"
    sql_where=(_username,_password)
    cursor.execute(sql,sql_where)
    row=cursor.fetchone()
    _username1=row[0]
    _password2=row[3]
    if _username1==_username:
        result=jsonify({'message':'you are logged in'})
    else:
        result=jsonify({'error':'sorry invalid username'})
    
    return result
app.run(debug=True)

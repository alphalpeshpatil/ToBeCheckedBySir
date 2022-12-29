#app.py
from flask import Flask, jsonify, make_response,request, session
import psycopg2
from datetime import datetime,timedelta
import jwt
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
        def user_login_model(self):
            cursor.execute(sql,sql_where)
            result=self.cursor.fetchall()
            userdata=result[0]
            exp_time=datetime.now() +timedelta(minutes=15)
            exp_epoch_time =int(exp_time.timestamp())
            payload={
                "payload":userdata,
                "exp":exp_epoch_time
            }
            jwtoken=jwt.encode(payload,"sagar",algorithm="HS256")
            result= make_response({"token":jwtoken},200)
    else:
        result=jsonify({'error':'sorry invalid username'})
    return result
app.run(debug=True)


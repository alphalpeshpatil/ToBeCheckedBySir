#app.py
from flask import Flask, jsonify, request, session
import psycopg2
app = Flask(__name__)
@app.route('/register',methods=['POST'])
def register():
    try:
        _json=request.json
        _username=_json['username']
        _lastname=_json['lastname']
        _email=_json['email']
        _password=_json['password']

        connection = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")
        cursor = connection.cursor()
        sql = """ INSERT INTO register (first_name,last_name,password,email) VALUES (%s,%s,%s,%s)"""
        sql_where=(_username,_lastname,_email,_password)
        cursor.execute(sql,sql_where)
        connection.commit()
        result=jsonify({'message':'registration done successufully'})
        return result
    except (Exception, psycopg2.Error) as error:
        result=jsonify({'sorry':'sorry'})
        return result
app.run(debug=True)

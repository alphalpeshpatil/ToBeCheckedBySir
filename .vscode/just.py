from flask import Flask,jsonify, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)


@app.route('/login', methods =['GET', 'POST'])
def login():
    print("hello world")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
        print(username)
        return jsonify({'message':'caught here'})
        # cursor = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")
        # cursor.execute('SELECT * FROM register WHERE username = % s AND password = % s', (username, password))
        # account = cursor.fetchone()
        # if account:
        #     session['password'] = account['password']
        #     session['username'] = account['username']
        #     return jsonify({'message' : 'you are logged in successfully'})
        # else:
        #     return jsonify({'message':'incorrect password or username'})
    print("end")
app.run(debug=True)
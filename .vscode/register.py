from flask import Flask,jsonify, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = psycopg2.connection.cursor(psycopg2.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
        psycopg2.connection.commit()
    return jsonify({'message':'your have registered'})
app.run(debug=True)

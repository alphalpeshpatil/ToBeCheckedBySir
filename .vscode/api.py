from flask import Flask
from flask import jsonify, request, session
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")

@app.route('/login', methods=['POST'])
def login():
	try:
		_json = request.json
		_username = _json['username']
		_password = _json['password']
				
		conn = psycopg2.connect()
		cursor = conn.cursor()
			
		sql = "SELECT * FROM register WHERE password=%s and username=%s"
		sql_where = (_username,_password)
		flag=0
		cursor.execute(sql, sql_where)
		row = cursor.fetchall()
		flag=1

		for row in row:
			_username=row[0]
			_password=row[3]
			flag=0

			if (flag == 1):
				return jsonify({'message' : 'you are logged in successfully'})
			else:
				resp = jsonify({'message' : 'invalid password'})
				resp.status_code = 400
				return resp
	except(Exception, psycopg2.Error) as error:
		print("Some error eccured")
app.run()
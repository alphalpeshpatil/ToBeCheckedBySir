from flask import Flask
from flask import jsonify, request, session
# from werkzeug import check_password_hash
import psycopg2
       
app = Flask(__name__)
connection = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")
@app.route('/login', methods=['POST'])
def login():
	try:
		_json = request.json
		_username = _json['username']
		_password = _json['password']
		
		# validate the received values
		if _username and _password:
			#check user exists			
			conn = psycopg2.connect()
			cursor = conn.cursor()
			
			sql = "SELECT * FROM user WHERE username=%s"
			sql_where = (_username,)
			
			cursor.execute(sql, sql_where)
			row = cursor.fetchone()
			
			if row:
				if check_password_hash(row[2], _password):
					session['username'] = row[1]
					#cursor.close()
					#conn.close()
					return jsonify({'message' : 'You are logged in successfully'})
				else:
					resp = jsonify({'message' : 'Bad Request - invalid password'})
					resp.status_code = 400
					return resp
		else:
			resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
			resp.status_code = 400
			return resp

	except Exception as e:
		print(e)
	
@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})
		
if __name__ == "__main__":
    app.run()


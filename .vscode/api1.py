from flask import Flask, request,jsonify
import json;

app = Flask(__name__)
@app.route('/search', methods=['GET'])
def search():
    args = request.args
    name = args.get('name')
    password = args.get('password')

    result = {name:password}
    return result
app.run(debug=True)


    
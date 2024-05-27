from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/')
@cross_origin(origin='*')
def hello_world():
    return 'Hello from Flask1!'

@app.route('/code2fab', methods=['POST'])
@cross_origin(origin='*')
def code2fab():
    req = request.json
    #return jsonify(req['code'])
    return request.json

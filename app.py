from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

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

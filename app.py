from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return 'Hello from Flask6!'

@app.route('/code2fab', methods=['POST'])
def code2fab():
    req = request.json
    #return jsonify(req['code'])
    return jsonify(request.json)



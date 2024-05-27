from flask import Flask, Response, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask1!'

@app.route('/code2fab', methods=['POST'])
def code2fab():
    req = request.json
    #return jsonify(req['code'])
    return request.json

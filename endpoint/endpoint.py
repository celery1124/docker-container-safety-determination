#!flask/bin/python
from flask import Flask, request
import json
import utils
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check_image', methods=['POST'])
def check_image():
    data = json.loads(request.data)
    print(data)
    print('success')
    return 'Done', 200

@app.route('/')
def index():
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

#!flask/bin/python
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/check_image', methods=['POST'])
def check_image():
    data = json.loads(request.data)
    print('success')
    return 'Done'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
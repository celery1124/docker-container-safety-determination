#!flask/bin/python
from flask import Flask, request
import json
import utils

app = Flask(__name__)
CORS(app)

@app.route('/check_image', methods=['POST'])
def check_image():
    data = json.loads(request.data)

    paths = utils.get_image_name(data)
    for p in paths:
	utils.pull_image(p)
	utils.save_image(p)
	utils.untar_image(p)
    return 'Done'

@app.route('/')
def index():
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

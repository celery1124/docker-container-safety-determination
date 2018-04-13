#!flask/bin/python
from flask import Flask, request
import json
import utils
import os
import global_check

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

        file_lst = []
        for root, dirs, files in os.walk('./test'):
            for name in files:
                print(os.path.join(root, name))
                file_lst.append(os.path.join(root, name))
        num_bad_files, suspicious_file_paths_list = global_check.global_process_files(file_lst)
        print('-------------------')
        print('num_bad_files: %d' %(num_bad_files))
        print('suspicious_file_paths_list: %s' %(suspicious_file_paths_list))
    return 'Done'

@app.route('/')
def index():
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

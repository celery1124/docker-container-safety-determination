#!flask/bin/python
from flask import Flask, request
import time
import json
import utils
import os
import global_check
import read_write_log


app = Flask(__name__)

@app.route('/check_image', methods=['POST'])
def check_image():
    data = json.loads(request.data)
    print(data)
    paths = utils.get_image_name(data)
    for p in paths:
        utils.pull_image(p)
        utils.save_image(p)
        utils.untar_image(p)

        file_lst = []
        for root, dirs, files in os.walk('./test'):
            for name in files:
                relative_path=os.path.join(root, name)
                abs_path=os.path.abspath(relative_path)
                print(abs_path)
                file_lst.append(abs_path)
        num_bad_files, suspicious_file_paths_list = global_check.global_process_files(file_lst)
        print('-------------------')
        print('num_bad_files: %d' %(num_bad_files))
        print('suspicious_file_paths_list: %s' %(suspicious_file_paths_list))

        # write line into log
        read_write_log.write_log(p, num_bad_files, suspicious_file_paths_list)
    return 'Done'

@app.route('/results', methods=['GET'])
def results():
    return read_write_log.read_log()

@app.route('/')
def index():
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)

from datetime import datetime
LOG_FILE = "registry-log.txt"


def write_log(p, num_bad_files, suspicious_file_paths_list):
    line = "<p>" + str(datetime.now()) + "; Image: " + p
    if num_bad_files == 0:
        line +=  "; OK\n</p>"
    else:
        line += "; Suspicious with files: </p><ul>"
        for suspicious_file_path in suspicious_file_paths_list:
            line += "<li>%s</li>" % suspicious_file_path 
        line += "</ul>"
    with open(LOG_FILE  , 'a') as file:
        file.write(line)

def read_log():
    with open(LOG_FILE, 'r') as content_file:
        content = content_file.read()
    return content

def test():
    p = ["d1", "d2", "d3"]
    num_bad_files = [1, 0, 2]
    suspicious_file_paths_list = [["path/f1"], [], ["path2", "path333"]]
    for i in range(0, 3):
        write_log(p[i], num_bad_files[i], suspicious_file_paths_list[i])
    print(read_log())

if __name__ == '__main__':
    test()

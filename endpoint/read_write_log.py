from datetime import datetime
LOG_FILE = "registry-log.txt"


def write_log(p, num_bad_files, suspicious_file_paths_list):
    line = str(datetime.now()) + " " + p
    if num_bad_files == 0:
        line +=  "OK\n"
    else:
        line += " Suspicious with files: \n"
        for suspicious_file_path in suspicious_file_paths_list:
            line += "\t%s\n" % suspicious_file_path 
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
    write_log(p[0], num_bad_files[0], suspicious_file_paths_list[0])
    for i in range(0, 3):
        write_log(p[i], num_bad_files[i], suspicious_file_paths_list[i])
    print(read_log())

if __name__ == '__main__':
    test()

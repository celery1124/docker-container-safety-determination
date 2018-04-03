from fuzzy_hash import sdhash_get_from_file
from virus_check import virus_check_file # take file path, return True for ok, False for virus
import os
from mongo_connect import connectMongo

CONTENT_GOOD = 1
CONTENT_SUSPICIOUS = 2

files_sdhashs = connectMongo()


def global_process_files(_file_paths_list):
    num_all_files = len(_file_paths_list)
    num_bad_files = 0
    suspicious_file_paths_list = []
    for file_path in _file_paths_list:
        head, file_name_with_ext = os.path.split(file_path) # with ext
        sdhash = sdhash_get_from_file(file_path)
        if global_check_file(file_name_with_ext, sdhash, file_path) == CONTENT_GOOD:
            print("One file passed global test")
        else:
            suspicious_file_paths_list.append(file_path)
            num_bad_files += 1
    return num_bad_files, suspicious_file_paths_list
            
def compare_sdhash_values(_in1, _in2):
    _med1 = _in1[_in1.find(":sha1:")]
    _med2 = _in1[_in2.find(":sha1:")]
    return _med1 == _med2
    
    
    
    
def global_check_file(file_name_with_ext, sdhash, file_path):
    record = files_sdhashs.find_one({"file": file_name_with_ext})
    if record == None:
        if not virus_check_file(file_path):
            return CONTENT_SUSPICIOUS
        record = {
            "file": file_name_with_ext,
            "num_sdhashs": 1,
            "sdhash0": sdhash
        }
        files_sdhashs.insert_one(record)
        return CONTENT_GOOD
    
    num_sdhashs = int(record["num_sdhashs"])
    for i in range(0, num_sdhashs):
        if compare_sdhash_values(sdhash, record["sdhash" + str(i)]):
            return CONTENT_GOOD
    # virus file
    if not virus_check_file(file_path):
        return CONTENT_SUSPICIOUS
    # file ok
    record["num_sdhashs"] = num_sdhashs + 1
    record["sdhash" + str(num_sdhashs)] = sdhash
    files_sdhashs.replace_one({"file": file_name_with_ext}, record)
    return CONTENT_GOOD


def test():
    test_files = ["./proposal.md", "./test/test1.md", "./test/test1/test1.md", "./test/test1/test2.md", "./test/test2/test1.md"]
    suspicious_file_paths_list = global_process_files(test_files)
    



if __name__ == "__main__":
    test()



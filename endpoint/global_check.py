from fuzzy_hash import sdhash_get_from_file
from virus_check import virus_check_file # take file path, return True for ok, False for virus
import os
from mongo_connect import connectMongo

CONTENT_GOOD = 1
CONTENT_SUSPICIOUS = 2

files_sdhashs = connectMongo()

def local_process_files(_file_paths_list):
    num_all_files = len(_file_paths_list)
    num_good_files = 0
    suspicious_file_paths_list = []
    for file_path in _file_paths_list:
        head, file_name_with_ext = os.path.split(file_path) # with ext
        sdhash = sdhash_get_from_file(file_path)
        if global_check_file(file_name_with_ext, sdhash, file_path) == CONTENT_GOOD:
            num_good_files += 1
        else:
            suspicious_file_paths_list.append(file_path)
    return suspicious_file_paths_list
            

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
        if sdhash == record["sdhash" + str(i)]:
            return CONTENT_GOOD
    # virus file
    if not virus_check_file(file_path):
        return CONTENT_SUSPICIOUS
    # file ok
    record["num_sdhashs"] = num_sdhashs + 1
    record["sdhash" + str(num_sdhashs)] = sdhash
    files_sdhashs.replace_one({"file": file_name_with_ext}, record)
    return CONTENT_GOOD





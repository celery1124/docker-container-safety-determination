from fuzzy_hash import sdhash_get_from_file
from fuzzy_hash import sdhash_compare_files
import os

CONTENT_GOOD = 1
CONTENT_SUSPICIOUS = 2
FILENAME_NOT_EXIST = 3


def local_process_files(_file_paths_list):
    num_all_files = len(_file_paths_list)
    num_good_files = 0
    suspicious_file_paths_list = []
    for file_path in _file_paths_list:
        head, file_name_with_ext = os.path.split(file_path) # with ext
        sdhash = sdhash_get_from_file(file_path)
        if check_db(file_name_with_ext, sdhash) == CONTENT_GOOD:
            num_good_files += 1
        else:
            suspicious_file_paths_list.append(file_path)
    return suspicious_file_paths_list
            

def check_db(file_name_with_ext, sdhash):
    pass

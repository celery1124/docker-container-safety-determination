# tested on Ubuntu 14.04, a cloud9 container
# Python 2.7 is supported

import fuzzyhashlib
from fuzzyhashlib import libssdeep_wrapper
import sdbf_class

# _in: the string to be calculate
def ssdeep_get(_in):
    return fuzzyhashlib.ssdeep(_in).hexdigest()
    
# two input args are original strings to be compared
def ssdeep_compare(_in_1, _in_2):
    ssdeep_1 = ssdeep_get(_in_1)
    ssdeep_2 = ssdeep_get(_in_2)
    return libssdeep_wrapper.compare(ssdeep_1, ssdeep_2)

# _in: file path, get the sdhash value from the file
def sdhash_get_from_file(_in):
    return sdbf_class.sdbf(_in, 0).to_string()

# two input args are original file paths to be compared
def sdhash_compare_files(_in_1, _in_2):
    sdbf_1 = sdbf_class.sdbf(_in_1, 0)
    sdbf_2 = sdbf_class.sdbf(_in_2, 0)
    return sdbf_1.compare(sdbf_2, 0)
    
# two input args are original file paths to be compared
def sdhash_compare(_in_1, _in_2):
    sdbf_1 = sdbf_class.sdbf(_in_1, 0)
    sdbf_2 = sdbf_class.sdbf(_in_2, 0)
    return sdbf_1.compare(sdbf_2, 0)

def test():
    s1 = "../proposal.md"
    s2 = "Also called fuzzy hashes, CTPH can match inputs that have homologies."
    s3 = "AlSo Called fuzzy hashes, CTPH can match inputs that have homologies."
    print(ssdeep_get(s2))
    print(sdhash_get_from_file(s1))
    
    print(ssdeep_compare(s2, s3))
    print(sdhash_compare_files(s1, s1))

if __name__ == "__main__":
    test()



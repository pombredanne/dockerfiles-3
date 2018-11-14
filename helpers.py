import json
import os
import pickle
import shutil
import fnmatch
import re

try:
    here = os.path.abspath(os.path.dirname(__file__))
except:
    here = os.getcwd()

root = os.path.join(here, "data")

# Helper Functions

def read_file(filename, mode="r"):
    with open(filename,mode) as filey:
        content = filey.read()
    return content

def write_file(filename, content, mode="w"):
    with open(filename, mode) as filey:
        if isinstance(content, list):
            for item in content:
                filey.writelines(content)
        else:
            filey.writelines(content)
    return filename


def has_python(dockerfile):
    '''determine if a Dockerfile has python, meaning mention of the term (python)
       or a command involving pip or conda. Return boolean to indicate yes/no!
    '''
    content = read_file(dockerfile)
    return bool(re.search('(python|conda|pip)', content))

def recursive_find(base, pattern=None):
    '''recursively find files that match a pattern, in this case, we will use
       to find Dockerfiles

       Paramters
       =========
       base: the root directory to start the seartch
       pattern: the pattern to search for using fnmatch
    '''
    if pattern is None:
        pattern = "*"

    for root, dirnames, filenames in os.walk(base):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)

def generate_catalog():
    '''for the index page, generate a Dataset Catalog (or Collection) that
       describes the entire set.'''


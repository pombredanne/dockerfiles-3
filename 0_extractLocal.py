#!/usr/bin/env python

import json
import os
import pickle
import shutil
import fnmatch
import re

# Helper Functions

def read_file(filename, mode="r"):
    with open(filename,mode) as filey:
        content = filey.read()
    return content

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


################################################################################
# Step 1. Measure delete operation
################################################################################

# Read in list of prefixes

here = os.path.abspath(os.path.dirname(__file__))

root = os.path.join(here, "data")
files = recursive_find(root, "Dockerfile")

originalCount = 0
finalCount = 0

# Do a check before deleting anything (delted won't be represented in repo)

for dockerfile in files:
    originalCount += 1
    if has_python(dockerfile):
        finalCount +=1

print('Found %s original files, %s of which have python.' %(originalCount, finalCount))
percentage = round(finalCount / originalCount * 100, 2)
print('This represents %s' % (percentage) + '% of files')
# Found 129519 original files, 33325 of which hae python.
# This represents 25.73% of files


################################################################################
# Step 2. Perform delete operation
################################################################################

files = recursive_find(root, "Dockerfile")

for dockerfile in files:
    if not has_python(dockerfile):
        dirname = os.path.dirname(dockerfile)
        shutil.rmtree(dirname)


################################################################################
# Step 3. Generate Metadata Pages, First for Dataset
################################################################################

from specifications.Dataset.extract import extract as dataset_extract
from specifications.SoftwareSourceCode.extract import extract as ssc_extract

#skipped = pickle.load(open('skipped.pkl','rb'))
#generated = pickle.load(open('generated.pkl','rb'))

files = recursive_find(root, "Dockerfile")
generated = {'dataset': set(), 'softwaresourcecode': set()}
skipped = {'dataset': set(), 'softwaresourcecode': set()}

for dockerfile in files:
    dirname = os.path.dirname(dockerfile)

    try:
        output_html = os.path.join(dirname, 'ssc.html')
        ssc_extract(dockerfile, output_html)
        generated['softwaresourcecode'].add(dockerfile)
    except:
        skipped['softwaresourcecode'].add(dockerfile)

    # If spython can't parse, skip for now
    try:
        output_html = os.path.join(dirname, 'dataset.html')
        dataset_extract(dockerfile, output_html)
        generated['dataset'].add(dockerfile)
    except:
        skipped['dataset'].add(dockerfile)


# Since ImageDefinition is larger, we will use sherlock
pickle.dump(skipped, open('skipped.pkl','wb'))
pickle.dump(generated, open('generated.pkl','wb'))

################################################################################
# Step 4. We will run container-diff (scaled) on sherlock
################################################################################

# This step is run locally to collect the image names

files = recursive_find(root, "Dockerfile")
names = set()

for dockerfile in files:
    name = '/'.join(os.path.dirname(dockerfile).split('/')[-2:])
    names.add(name)
    
pickle.dump(names, open('names.pkl','wb'))
# scp next to sherlock

#!/usr/bin/env python

import json
import os
import pickle

from helpers import *

################################################################################
# Step 1. Measure delete operation
################################################################################

# Read in list of prefixes
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
from specifications.ImageDefinition.extract import extract as def_extract

#generated = {'dataset': set(), 'softwaresourcecode': set(), 'imagedef': set()}
#skipped = {'dataset': set(), 'softwaresourcecode': set(), 'imagedef': set()}

skipped = pickle.load(open('skipped.pkl','rb'))
generated = pickle.load(open('generated.pkl','rb'))
files = recursive_find(root, "Dockerfile")

for dockerfile in files:
    dirname = os.path.dirname(dockerfile)

    try:
        output_html = os.path.join(dirname, 'ImageDefinition.html')
        def_extract(dockerfile, output_html)
        generated['imagedef'].add(dockerfile)
    except:
        skipped['imagedef'].add(dockerfile)

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

# This didn't actually work, we need to do changes to container-diff to run
# in a cluster environment
# https://github.com/GoogleContainerTools/container-diff/pull/274
# https://github.com/GoogleContainerTools/container-diff/issues/275

#!/usr/bin/env python

import json
import os
import pickle

from helpers import ( recursive_find, read_file, root )

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
from specifications.DataCatalog.extract import extract as catalog_extract
from specifications.Organization.extract import extract as org_extract

generated = {'Dataset': set(), 
             'SoftwareSourceCode': set(), 
             'ImageDefinition': set()}

skipped = {'Dataset': set(), 
           'SoftwareSourceCode': set(), 
           'ImageDefinition': set()}

files = recursive_find(root, "Dockerfile")

# Generate the DataCatalog and organization
catalog = catalog_extract()
contact = org_extract()

for dockerfile in files:
    dirname = os.path.dirname(dockerfile)

    try:
        output_html = os.path.join(dirname, 'SoftwareSourceCode.html')
        ssc_extract(dockerfile, output_html)
        generated['SoftwareSourceCode'].add(dockerfile)
    except:
        skipped['SoftwareSourceCode'].add(dockerfile)

    # If spython can't parse, skip for now
    try:
        output_html = os.path.join(dirname, 'Dataset.html')
        dataset_extract(dockerfile, output_html, catalog, contact)
        generated['Dataset'].add(dockerfile)
    except:
        skipped['Dataset'].add(dockerfile)


# Since ImageDefinition is larger, we will use sherlock
pickle.dump(skipped, open('skipped.pkl','wb'))
pickle.dump(generated, open('generated.pkl','wb'))

# See README for steps to use cluster extract scripts, then generate.py
# to finish up work.

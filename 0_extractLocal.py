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

generated = {'Dataset': set(), 
             'SoftwareSourceCode': set(), 
             'ImageDefinition': set()}

skipped = {'Dataset': set(), 
           'SoftwareSourceCode': set(), 
           'ImageDefinition': set()}

#skipped = pickle.load(open('skipped.pkl','rb'))
#generated = pickle.load(open('generated.pkl','rb'))
files = recursive_find(root, "Dockerfile")

# Generate the DataCatalog
catalog = catalog_extract()

for dockerfile in files:
    dirname = os.path.dirname(dockerfile)

    ssc = os.path.join(dirname, 'ssc.html')
    ds = os.path.join(dirname, 'dataset.html')
    for old in [ssc, ds]:
        if os.path.exists(old):
            os.remove(old)

    try:
        output_html = os.path.join(dirname, 'SoftwareSourceCode.html')
        ssc_extract(dockerfile, output_html)
        generated['SoftwareSourceCode'].add(dockerfile)
    except:
        skipped['SoftwareSourceCode'].add(dockerfile)

    # If spython can't parse, skip for now
    try:
        output_html = os.path.join(dirname, 'Dataset.html')
        dataset_extract(dockerfile, output_html, catalog)
        generated['Dataset'].add(dockerfile)
    except:
        skipped['Dataset'].add(dockerfile)


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

# Then need to update the generated and skipped data structures with result
from specifications.ImageDefinition.extract import extract as def_extract

# This didn't actually work, we need to do changes to container-diff to run
# in a cluster environment
# https://github.com/GoogleContainerTools/container-diff/pull/274
# https://github.com/GoogleContainerTools/container-diff/issues/275


################################################################################
# Step 5. Generate Example Index (Table) for Dataset
################################################################################

from specifications.DataCatalog.extract import extract as catalog_extract
catalog = catalog_extract()

template = read_file('template.html')
template = template.replace('{{ SCHEMAORG_TYPE }}', "Dataset")

# Generate list of rows to plug into template
rows = []
for dataset in list(generated['Dataset']):
    folder = os.path.dirname(dataset)
    subfolder = folder.split('/')[-3:]
    name = '/'.join(subfolder)
    uri = '/'.join(subfolder[0:2])
    row = '''<tr><td>
                 <a href="https://openschemas.github.io/dockerfiles/data/%s/Dataset.html">%s</a>
             </td></tr>''' %(name, uri)
    rows.append(row)

template = template.replace('{{ CLUSTERIZE_TABLE }}', '\n'.join(rows))
write_file('index.html', template)

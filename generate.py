#!/usr/bin/env python

import json
import os
import pickle

from helpers import ( recursive_find, read_file, write_file, root )

################################################################################
# Step 1. Index the files generated with container-diff on Sherlock
#         The json files should be in the container-diff folder locally
################################################################################

diffs = recursive_find('container-diff', '*.json')
diff_names = []
for diff in diffs:
    try:
        d = json.load(open(diff,'r'))
        diff_names.append(d[0]['Image'])
    except:
        print('Problem parsing %s' % diff)
        pass

# Just one problem parsing!
# Problem parsing container-diff/jimwhite-bllip-parser-python.json

# How many do we have total?
# 54592
len(diff_names)
pickle.dump(diff_names, open('container-diff-names.pkl','wb'))

################################################################################
# Step 2. Generate subfolders with pages, each is a subset according to
#         the first letter
################################################################################

from specifications.DataCatalog.extract import extract as catalog_extract
catalog = catalog_extract()

# Oraganize containers by first letter
letters = dict()
for dataset in diff_names:
    letter = dataset[0]
    if letter not in letters:
        letters[letter] = []
    row = '''<tr><td>
                 <a href="https://openschemas.github.io/dockerfiles/data/%s/%s/ImageDefinition.html">%s</a>
             </td></tr>''' %(letter, dataset, dataset)
    letters[letter].append(row)

pickle.dump(letters, open('container-diff-letters.pkl','wb'))
letters = pickle.load(open('container-diff-letters.pkl', 'rb'))
diff_names = pickle.load(open('container-diff-names.pkl', 'rb'))

# put into output directory
if not os.path.exists('pages'):
    os.mkdir('pages')

# Now write into html pages
from schemaorg.templates.google import make_table

table = []

for letter, rows in letters.items():
    content = '''<a href="https://openschemas.github.io/dockerfiles/pages/%s/">
        <img src="https://via.placeholder.com/150/e16a3f/FFFFFF/?text=%s" data-full="https://via.placeholder.com/350/e16a3f/FFFFFF/?text=%s" 
                class="m-p-g__thumbs-img"></img></a>''' %(letter, letter.upper(), letter.upper())
    table.append(content)
    outdir = 'pages/%s' %letter
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    make_table(catalog, rows,
               title = "Dataset: Dockerfile Letter %s" %letter,
               output_file="%s/index.html" %outdir)

template = read_file('template.html')
template = template.replace('{{ SCHEMAORG_TABLE }}', '\n'.join(table))
template = template.replace('{{ SCHEMAORG_JSON }}', catalog.dump_json())
write_file('index.html', template)


################################################################################
# Step 3. Generate the ImageDefinition files for each container-diff
################################################################################

# Then need to update the generated and skipped data structures with result
from specifications.ImageDefinition.extract import extract as def_extract
from specifications.DataCatalog.extract import extract as catalog_extract
from specifications.Organization.extract import extract as org_extract

# This originally didn't work, we needed to do changes to container-diff to run
# in a cluster environment
# https://github.com/GoogleContainerTools/container-diff/pull/274
# https://github.com/GoogleContainerTools/container-diff/issues/275
# https://github.com/GoogleContainerTools/container-diff/pull/279

# Generate the DataCatalog and organization
catalog = catalog_extract()
contact = org_extract()

for diff in diff_names:
    
    letter = diff[0]
    dirname = os.path.abspath('data/%s/%s' %(letter, diff))

    # Find the container-diff
    file_name = diff.replace('/','-')
    container_diff_file = os.path.join('container-diff', '%s.json' % file_name)

    try:
        dockerfile = os.path.join(dirname, 'Dockerfile')
        output_html = os.path.join(dirname, 'ImageDefinition.html')
        if not os.path.exists(output_html):
            res = def_extract(dockerfile, diff, output_html, container_diff_file)
    except:
        pass

# Done!

#!/usr/bin/env python

import json
import os
import pickle
import shutil
import fnmatch
import re

# Make directory for working
# module load python/3.6.1
# pip install --user spython
# pip install --user schemaorg
# pip install --user ipython

base = "/scratch/users/vsochat/WORK/dockerfiles"
os.chdir(base)
os.mkdir('.job')
os.mkdir('.out')
names_pkl = os.path.join(base, 'names.pkl')
output_dir = os.path.join(base, 'container-diff')
os.mkdir(output_dir)
names = pickle.load(open(names_pkl,'rb'))

# For each container, run a container-diff job
for name in names:
    print("Processing %s" % name)
    filename = name.replace('/','-')
    file_name = ".job/%s.job" %(filename)
    output_pkl = os.path.join(output_pkl, '%s.pkl' % filename)
    with open(file_name, "w") as filey:
        filey.writelines("#!/bin/bash\n")
        filey.writelines("#SBATCH --job-name=%s\n" %filename)
        filey.writelines("#SBATCH --output=.out/%s.out\n" %filename)
        filey.writelines("#SBATCH --error=.out/%s.err\n" %filename)
        filey.writelines("#SBATCH --time=60:00\n")
        filey.writelines("#SBATCH --mem=8000\n")
        filey.writelines('module load python/3.6.1')
        filey.writelines("python 1_extractSherlock.py %s %s\n" % output_pkl, name)
        os.system("sbatch -p owners .job/%s.job" %filename)

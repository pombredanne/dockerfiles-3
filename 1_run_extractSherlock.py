#!/usr/bin/env python

import os
import pickle
import time

# Make directory for working
# module load python/3.6.1
# pip install --user spython
# pip install --user schemaorg
# pip install --user ipython

base = "/scratch/users/vsochat/WORK/dockerfiles"
os.chdir(base)

names_pkl = os.path.join(base, 'names.pkl')
output_dir = os.path.join(base, 'container-diff')
names = pickle.load(open(names_pkl,'rb'))

for dirname in ['.job', '.out', output_dir]:
    if not os.path.exists(dirname):
        os.mkdir(dirname)

# cache directory for layers
cache_dir = "/scratch/users/vsochat/.singularity/docker"

# Function to ensure we don't go over job limit (1000)
def count_queue():
    user = os.environ['USER']
    return int(os.popen('squeue -u %s | wc -l' %user).read().strip('\n'))


# Step 2. Generate jobs, add any that don't get to run to list
jobs = []
job_limit = 1000

count = count_queue()

# There are a total of X names, 

# For each container, run a container-diff job
for name in names:
    print("Processing %s" % name)
    filename = name.replace('/','-')
    file_name = ".job/%s.job" %(filename)
    output_json = os.path.join(output_dir, '%s.json' % filename)
    if not os.path.exists(output_json):
        if count < job_limit:
            with open(file_name, "w") as filey:
                filey.writelines("#!/bin/bash\n")
                filey.writelines("#SBATCH --job-name=%s\n" %filename)
                filey.writelines("#SBATCH --output=.out/%s.out\n" %filename)
                filey.writelines("#SBATCH --error=.out/%s.err\n" %filename)
                filey.writelines("#SBATCH --time=30:00\n")
                filey.writelines("#SBATCH --mem=8000\n")
                filey.writelines('module load python/3.6.1\n')
                filey.writelines("/bin/bash 1_extractSherlock.sh %s %s %s\n" % (output_json, name, cache_dir))
                filey.writelines("rm .job/%s.job\n" % filename)
                filey.writelines("rm .out/%s.out" % filename)
                filey.writelines("rm .out/%s.err" % filename)

            os.system("sbatch -p owners .job/%s.job" %filename)
        else:
            jobs.append(file_name)
            time.sleep(1)

# /bin/bash 1_extractSherlock.sh /scratch/users/vsochat/WORK/dockerfiles/container-diff/alerta-alerta-web.json alerta/alerta-web /scratch/users/vsochat/.singularity/docker

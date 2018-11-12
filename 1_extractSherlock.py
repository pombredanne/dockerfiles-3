#!/usr/bin/env python

import json
import os
import pickle
import re
import sys
from spython.utils import run_command

# Read in arguments
output_pkl = sys.argv[1]
uri = sys.argv[2]

if os.path.exists(output_pkl):
    print('File %s already exists, exiting.' %output_pkl)
    sys.exit(0)

# Container Diff
response = run_command(["container-diff", "analyze", uri,
                        "--type=pip", "--type=apt", "--type=history",
                        "--json", '--quiet','--verbosity=panic'])

# softwareRequirements
requires = [] # APT and PIP

# note that the top level key here can be history, files, pip, apt, etc.
if response['return_code'] == 0:
    layers = json.loads(response['message'][0])
    for layer in layers:
        ## Pip and Apt will go into softwareRequirements
        if layer['AnalyzeType'] in ["Pip","Apt"]:
            for pkg in layer['Analysis']:
                requires.append('%s > %s==%s' %(layer['AnalyzeType'],
                                                pkg['Name'],
                                                pkg['Version']))         


layers['requires'] = requires
pickle.dump(open(output_pkl, 'wb'))

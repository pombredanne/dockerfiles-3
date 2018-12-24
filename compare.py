#!/usr/bin/env python

import json
import os
import pandas
import pickle

# module load python/3.6.1
# module load py-pandas/0.23.0_py36
# module load py-ipython/6.1.0_py36

from helpers import ( recursive_find, read_file, write_file, root )

# In these sections, we will extract packages from Pip And Apt, and do it
# separately because the data structures are very big.

################################################################################
# Pip
################################################################################

# Let's create a simple data frame that looks at python libraries, even without
# versions

diffs = recursive_find('container-diff', '*.json')
features = set()
for diff in diffs:
    try:
        data = json.load(open(diff,'r'))
        for analysis in data:
            analysis_type = analysis['AnalyzeType']
            if analysis_type == 'Pip':
                new_features = ['%s__%s' %(analysis_type, a['Name']) for a in analysis['Analysis']]
                features = features.union(set(new_features))
    except: 
        print('Problem parsing %s' % diff)
        pass


len(features)
# 4687

pickle.dump(features, open('feature-set-4k.pkl', 'wb'))
features = pickle.load(open('feature-set-4k.pkl', 'rb'))
# Now create a feature vector, for each, with corresponding packages

diffs = recursive_find('container-diff', '*.json')
df = pandas.DataFrame(columns=list(features))
for diff in diffs:
    try:
        data = json.load(open(diff,'r'))
        for analysis in data:
            analysis_type = analysis['AnalyzeType']
            image_uri = analysis['Image']
            if analysis_type in ['Pip'] and image_uri not in df:
                new_features = ['%s__%s' %(analysis_type, a['Name']) for a in analysis['Analysis']]
                df.loc[image_uri, new_features] = 1
    except: 
        print('Problem parsing %s' % diff)
        pass

len(list(recursive_find('container-diff', '*.json')))
# Out of the total of 54593 containers, 42055 have Pip packages

# Note that on the first go we only read about 6K of these.
df[df.isna()==True] = 0
df.to_csv('feature-set-df-42k.csv')
df.to_pickle('feature-set-df-42k.pkl')

df = pandas.read_pickle('feature-set-df-42k.pkl')
df.shape
# (42055, 4687)

# Finally, let's make a crude list of labels to color container by (guessed) OS / base image
# This is run on my local machine where the data files are
from spython.main.parse import DockerRecipe

fromheaders = []
for uri in df.index.tolist():
    try:
        letter = uri[0]
        image_def = os.path.abspath('data/%s/%s/Dockerfile' %(letter, uri))
        if os.path.exists(image_def):
            result = DockerRecipe(image_def)            
            fromheaders.append(result.fromHeader)
        else:
            fromheaders.append('unknown')
    except: 
        print('Problem parsing %s' % uri)
        pass

# Let's parse just the image name, without the tag
fromheaders_notag = [x.split(':')[0] for x in fromheaders]

# Now we will remove any library (username)
fromheaders_containers = [x.split('/')[0] for x in fromheaders_notag]

# That looks pretty good! Save all three
labels = {'notag': fromheaders_notag,
          'images': fromheaders_containers,
          'fromheaders': fromheaders,
          'original': df.index.tolist() }

pickle.dump(labels, open('df-labels-42k.pkl', 'wb'))



################################################################################
# Apt
################################################################################

diffs = recursive_find('container-diff', '*.json')
features = set()
for diff in diffs:
    try:
        data = json.load(open(diff,'r'))
        for analysis in data:
            analysis_type = analysis['AnalyzeType']
            if analysis_type == 'Apt':
                new_features = ['%s__%s' %(analysis_type, a['Name']) for a in analysis['Analysis']]
                features = features.union(set(new_features))
    except: 
        print('Problem parsing %s' % diff)
        pass


len(features)
# 28226

pickle.dump(features, open('feature-apt-28k.pkl', 'wb'))
features = pickle.load(open('feature-apt-28k.pkl', 'rb'))
# Now create a feature vector, for each, with corresponding packages

diffs = recursive_find('container-diff', '*.json')
df = pandas.DataFrame(columns=list(features))
count = 0
for diff in diffs:
    try:
        data = json.load(open(diff,'r'))
        if count % 1000 == 0:
            df.to_pickle('feature-set-df-apt.pkl')
        for analysis in data:
            analysis_type = analysis['AnalyzeType']
            image_uri = analysis['Image']
            if analysis_type in ['Apt'] and image_uri not in df:
                new_features = ['%s__%s' %(analysis_type, a['Name']) for a in analysis['Analysis']]
                df.loc[image_uri, new_features] = 1
        count+=1
    except: 
        print('Problem parsing %s' % diff)
        pass
    

len(list(recursive_find('container-diff', '*.json')))
# Out of the total of 54593 containers, 42055 have Pip packages

# Note that on the first go we only read about 6K of these.
df[df.isna()==True] = 0
df.to_csv('feature-set-df-42k.csv')
df.to_pickle('feature-set-df-42k.pkl')

df = pandas.read_pickle('feature-set-df-42k.pkl')
df.shape
# (42055, 4687)

# Finally, let's make a crude list of labels to color container by (guessed) OS / base image
# This is run on my local machine where the data files are
from spython.main.parse import DockerRecipe

fromheaders = []
for uri in df.index.tolist():
    try:
        letter = uri[0]
        image_def = os.path.abspath('data/%s/%s/Dockerfile' %(letter, uri))
        if os.path.exists(image_def):
            result = DockerRecipe(image_def)            
            fromheaders.append(result.fromHeader)
        else:
            fromheaders.append('unknown')
    except: 
        print('Problem parsing %s' % uri)
        pass

# Let's parse just the image name, without the tag
fromheaders_notag = [x.split(':')[0] for x in fromheaders]

# Now we will remove any library (username)
fromheaders_containers = [x.split('/')[0] for x in fromheaders_notag]

# That looks pretty good! Save all three
labels = {'notag': fromheaders_notag,
          'images': fromheaders_containers,
          'fromheaders': fromheaders,
          'original': df.index.tolist() }

pickle.dump(labels, open('df-labels-42k.pkl', 'wb'))

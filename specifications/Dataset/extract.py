#!/usr/bin/env python

'''
This function will demonstrate how we can extract metadata from a Dockerfile,
and then generate a (html) web template to serve with it so that it is
able to be indexed by Google Datasets as a Dataset. No, a container is not
a Dataset, but this is the best tag we have at the moment. 

Author: @vsoch
November 11, 2018

    Thing > Dataset

To help move forward the effort, please see:

 - https://groups.google.com/a/opencontainers.org/forum/#!topic/dev/vEupyIGtvJs
 - https://github.com/schemaorg/schemaorg/issues/2059#issuecomment-427208907

'''

from schemaorg.templates.google import ( make_person, make_dataset )
from schemaorg.main.parse import RecipeParser
from schemaorg.main import Schema
from spython.main.parse import DockerRecipe
import os


def extract(dockerfile, output_file):
    '''extract a dataset from a given dockerfile, write to html output file.
       Yes, the person is hardcoded as @vsoch the Dinosaur. This is my example
       and I can do that.
    '''

    # Step 0. Define absolute paths to our Dockerfile, recipe, output
    here = os.path.abspath(os.path.dirname(__file__))
    recipe_yml = os.path.join(here, "recipe.yml")
    

    # Step 1: Show required and recommended fields from recipe
    recipe = RecipeParser(recipe_yml)
    
    # Step 2: Generate a Person (these are Google Helper functions)
    person = make_person(name="@vsoch",
                         description='research software engineer, dinosaur')

    # Step 3: Create Dataset
    parser = DockerRecipe(dockerfile)
    dataset = Schema("Dataset")

    # dataset.properties
    dataset.add_property('creator', person)
    dataset.add_property('version', dataset.version)
    dataset.add_property('description', 'A Dockerfile build recipe')
    dataset.add_property('name', parser.fromHeader)

    # Fun properties :)
    dataset.add_property('thumbnailUrl', 'https://vsoch.github.io/datasets/assets/img/avocado.png')
    dataset.add_property('sameAs', ['ImageDefinition', 'SoftwareSourceCode'])
    dataset.add_property('about', 'This is a Dockerfile provided by the Dinosaur Dataset collection.')

    # Step 4: Validate Data Structure
    recipe.validate(dataset)
    return make_dataset(dataset, output_file)

#!/usr/bin/env python

'''
This script will provide a function for extracting information from a Dockerfile
as a softwareSourceCode.

Author: @vsoch
October 21, 2018

    Thing > CreativeWork > SoftwareSourceCode

But for this first example, we will only use
specifications that are "official" and defined in schema.org so we stop
at "SoftwareSourceCode"

    Thing > CreativeWork > SoftwareSourceCode

If you think this is wrong, then put your money where your mouth is
and help the community to define the right spot. :)

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
    ssc = Schema("SoftwareSourceCode")

    # dataset.properties
    ssc.add_property('creator', person)
    ssc.add_property('version', ssc.version)
    ssc.add_property('description', 'A Dockerfile build recipe')
    ssc.add_property('name', parser.fromHeader)

    # Fun properties :)
    ssc.add_property('thumbnailUrl', 'https://vsoch.github.io/datasets/assets/img/avocado.png')
    ssc.add_property('sameAs', 'ImageDefinition')
    ssc.add_property('about', 'This is a Dockerfile provided by the Dinosaur Dataset collection.')
    ssc.add_property('codeRepository', 'https://www.github.com/openschemas/dockerfiles')
    ssc.add_property('runtime', 'Docker')

    # Step 4: Validate Data Structure
    recipe.validate(ssc)
    return make_dataset(ssc, output_file)

#!/usr/bin/env python

'''
This function will demonstrate how we can generate a DataCatalog
Author: @vsoch
November 13, 2018

    Thing > DataCatalog

'''

from schemaorg.templates.google import make_dataset
from schemaorg.main.parse import RecipeParser
from schemaorg.main import Schema
import os


def extract(output_file=None):
    '''extract a DataCatalog to describe some dataset. 
    '''

    # Step 0. Define absolute paths to our Dockerfile, recipe, output
    here = os.path.abspath(os.path.dirname(__file__))
    recipe_yml = os.path.join(here, "recipe.yml")
    
    # Step 3: Create Data Catalog
    catalog = Schema("DataCatalog")

    # Step 1: Show required and recommended fields from recipe
    recipe = RecipeParser(recipe_yml)
    
    # datacatalog.properties
    catalog.add_property('url', "https://openschemas.github.io/dockerfiles")
    catalog.add_property('name', "Dinosaur Dataset: Dockerfiles (python subset)")
    catalog.add_property('description', 'A small (30K) example database of Dockerfile build recipes')
    catalog.add_property('thumbnailUrl', 'https://vsoch.github.io/datasets/assets/img/avocado.png')
    catalog.add_property('about', 'This is a small dataset of Dockerfiles provided by the Dinosaur Dataset collection.')

    # Step 4: Validate Data Structure
    recipe.validate(catalog)
    return catalog

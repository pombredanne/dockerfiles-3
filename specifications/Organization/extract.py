#!/usr/bin/env python

'''
This function will demonstrate how we can generate an Organization
Author: @vsoch
November 14, 2018

    Thing > Organization

'''

from schemaorg.main.parse import RecipeParser
from schemaorg.main import Schema
import os


def extract(output_file=None):
    '''derive an Organization
    '''

    # Step 1. Define absolute paths to our recipe file
    here = os.path.abspath(os.path.dirname(__file__))
    recipe_yml = os.path.join(here, "recipe.yml")
    
    # Step 2: Create Contact Point
    contact = Schema("ContactPoint")
    contact.add_property('contactType', 'customer support')
    contact.add_property('telephone', "+1-650.721.4040")
    contact.add_property('email', 'research-computing-support@stanford.edu')

    # Step 3: Show required and recommended fields from recipe
    recipe = RecipeParser(recipe_yml)
    
    # Organization properties
    org = Schema("Organization")
    org.add_property('contactPoint', contact)
    org.add_property('url', "https://srcc.stanford.edu/about")
    org.add_property('name', "Stanford University > Research Computing Support Center")

    # Step 4: Validate Data Structure
    recipe.validate(org)
    return org

# Dockerfiles as ImageDefinition

This is a fork of the dockerfiles [Dinosaur Dataset](https://vsoch.github.io/datasets), with the goal
being to test using the [schema.org](https://www.schema.org) Dataset, SoftwareSourceCode, and 
ContainerRecipe (under development) representations of the containers to make them accessible
with Google Search.

<a target="_blank" href="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67"><img src="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67" alt="https://vsoch.github.io/datasets/assets/img/avocado.png" data-canonical-src="https://vsoch.github.io/datasets/assets/img/avocado.png" style="max-width:100%; float:right" width="200px"></a>

For generation of the Dockerfiles, see the [dockerfiles](https://www.github.com/vsoch/dockerfiles) Github repository.

## Generation

The following steps are covered in the [generate.py](generate.py) script provided here. The script does the following:

 1. We are interested in a subset of the data, so we choose "python applications" and thus recursively walk through the original dataset folders and remove those that don't have pip, conda, or python in the build recipe.
 3. We use the [schemaorg example](https://github.com/openbases/extract-dockerfile) to generate an ImageDefinition, Dataset, and SoftwareSourceCode example, one for each, along with generating a datastructure with links to each (that we can use later to create some search interface).

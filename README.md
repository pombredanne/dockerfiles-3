# Dockerfiles as ContainerRecipe

This is a fork of the dockerfiles [Dinosaur Dataset](https://vsoch.github.io/datasets), with the goal
being to test using the [schema.org](https://www.schema.org) Dataset, SoftwareSourceCode, and 
ContainerRecipe (under development) representations of the containers to make them accessible
with Google Search.

<a target="_blank" href="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67"><img src="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67" alt="https://vsoch.github.io/datasets/assets/img/avocado.png" data-canonical-src="https://vsoch.github.io/datasets/assets/img/avocado.png" style="max-width:100%; float:right" width="100px"></a>

For generation of the Dockerfiles, see the [dockerfiles](https://www.github.com/vsoch/dockerfiles) Github repository.

## Generation

 1. We are interested in a subset of the data, so we choose "python applications" and thus recursively walk through the original dataset folders and remove those that don't have pip or python in the build recipe. We start with X dockerfiles, and after this step are left with X. We do this with the script [0_pythonFilter.py].

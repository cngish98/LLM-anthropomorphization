# LLM Anthropomorphization

LING 472 / ANLY 521 Final Project | Spring 2023

[Jess Cusi](https://github.com/jessicacusi), [Caroline Gish](https://github.com/cngish98), [Cindy Li](https://github.com/cjlicjli)

## Background

### [Presentation Slides](https://docs.google.com/presentation/d/1goQKjHUAjKexrbL4J1h_FJL5pZiMgEDOUCAEMbnUXoI/edit#slide=id.p)

## Running the Project

### Set up & Installation

To install packages:

```commandline
conda env create --name llm --file environment.yml 
```

To install the project:

```
pip install -e .
```

To add required packages to the environment.yml

```commandline
conda env export > environment.yml --no-builds
```

## Development

Code is formatted with `black`. 

To update enivornment.yml after changing dependencies, run `conda env export environment.yml`

## Data 

For information about the data we used and how to retrieve it yourself, see [scraper](/scraper).
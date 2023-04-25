# LLM Anthropomorphization

LING 472 / ANLY 521 Final Project | Spring 2023

[Jess Cusi](https://github.com/jessicacusi), [Caroline Gish](https://github.com/cngish98), [Cindy Li](https://github.com/cjlicjli)

## Background

### [Presentation Slides](https://docs.google.com/presentation/d/1ZHLGu2YBoXJVcdEjcOy1eXtJxd5EY-3f_f3NjuFypEo/edit?usp=sharing)

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

## Development

Code is formatted with `black`. 


To add required packages to the environment.yml

```commandline
conda env export > environment.yml --no-builds
```

## Data 

For information about the data we used and how to retrieve it yourself, see [scraper](/scraper).

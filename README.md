# LLM Anthropomorphization

LING 472 / ANLY 521 Final Project | Spring 2023

[Jess Cusi](https://github.com/jessicacusi), [Caroline Gish](https://github.com/cngish98), [Cindy Li](https://github.com/cjlicjli)

## Background

### [Presentation Slides](https://docs.google.com/presentation/d/1goQKjHUAjKexrbL4J1h_FJL5pZiMgEDOUCAEMbnUXoI/edit#slide=id.p)

## Development

### Set up & Installation

To install packages:

```commandline
conda env create --name llm --file environment.yml 
```

To add required packages to the environment.yml

```commandline
conda env export > environment.yml --no-builds
```

To install the project:

```
pip install -e .
```

### Formatting

Code is formatted with `black`.

## Data

For information about the data we used and how to retrieve it yourself, see [scraper](/scraper). The paths provided
assume your data directory is on the same level as llm-anthropomorphization. If your data is stored elsewhere, make sure
to adjust the path.

## Running the Project

```commandline
cd labeler/bin
python main.py --data <data> --process <baseline,model> --export
```

- [required] `data` is the location of your data files
- [required] `process` indicates whether you want to run the baseline labeler or model labeler. for the model labeler,
  baseline is
  still run first.
- [optional] `export` will write baseline output to csv

For example, this command runs the baseline labeler against the labeled data in our private repository and will not
write the baseline labeled output to csv.

```commandline
python main.py -d ../../../llm-data/labeled-data/ -p baseline
```


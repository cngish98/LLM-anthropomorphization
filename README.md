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

As a one-time action, make sure to install CoreNLP. The simplest way will be to run `stanza.install_corenlp()` but other
options can be found in their [documentation](https://stanfordnlp.github.io/stanza/client_setup.html).

To install the project:

```
pip install -e .
```

## Development

Code is formatted with `black`. 
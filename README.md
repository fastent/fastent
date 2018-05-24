# fastent

The **fastent** Python library is a tool for end-to-end creation of **custom models for named-entity recognition**.

#### Custom Models

To train a model for a new type of entity, you just need a list of examples.

You are not limited to only predefined types like person, location and organization.

#### How It Works

fastent does end-to-end creation: **dataset generation**, **annotation**, **contextualiziation** and **training** a model.

You can also use fastent modules as standalone tools.


#### Made for Prod

fastent includes integrations with tools like spaCy, fastText pre-trained models and NLTK.

fastent is built to scale to very large text datasets in many languages.


How well does it work?  See the baseline performance on diverse [benchmarks](/benchmarks).

How can you get started?  Read on!

Table of contents
=================

<!--ts-->
 * [Installation](#installation)
 * [Usage](#usage)
    * [Dataset generation](#Dataset-Generation)
    * [Contextualization](#Contextualization)
    * [Api for model download](#Api)
    * [Annotation](#Annotation)
    * [Text utilities](#Text-utilities)
    * [wordnet utilities](#Wordnet)
    * [Poincare embeddings wrapper](#Poincare)
    * [Combinging everyting](#combo)
 * [Baselines](#tests)
 * [Dependency](#dependency)
<!--te-->


## Installation

fastent is developed for Python 3.

Clone this repo or install from PyPI:
```
pip install fastent
```

Install and set up CouchDB

For Unix systems:
```
wget -O - https://raw.githubusercontent.com/fastent/fastent/master/install.sh | bash
```

Download NLTK data:
```
python - << "EOF"
import nltk
nltk.download('stopwords')
EOF
```

#### Downloading data files
TODO: fastText stuff

### Generation

fastent can generate a dataset from a list

TODO

fastent can even generate a list from one or two examples.
```
from fastent import dataset_pseudo_generator

model = dataset_pseudo_generator.spacy_initialize('en_core_web_lg')
dataset_pseudo_generator.dataset_generate(model,['cocaine', 'heroin'], 100)
```

The equivalent on the command line:
```
python dataset_pseudo_generator.py -m en_core_web_lg -s cocaine,heroin
```

### Annotation

TODO

### Contextualization

TODO

### Training
To train a model from the annotated and contextualized dataset:

For now the only supported learning framework is spaCy.

[Request support for a new learning framework](https://github.com/fastent/fastent/issues/new?labels=Models&title=New+learning+framework+support+request:)

TODO: sample output

### Testing

Coming soon!



# fastent

The **fastent** Python library is a tool for end-to-end creation of **custom models for named-entity recognition**.

#### Custom Models

To train a model for a new type of entity, you just need a list of examples.

You are not limited to only predefined types like person, location and organization.

#### Features

fastent does end-to-end creation: dataset generation, annotation, contextualiziation and training.

You can also use fastend modules as standalone tools.


#### Made for Prod

fastent includes integrations with tools like spaCy, fastText pre-trained models and NLTK.

fastent is built to scale to very large text datasets in many languages.


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


Installation
============

This section show the process for installing the package with different methods

### From source

1) lets start by cloning the package

``` 
git clone https://github.com/fastent/fastent.git
```
2) Installing all the relevant packages

``` 
pip install -r requirements.txt 
```

3) Install couchDB 

Update the current packages
```
sudo apt-get update
```

Adding PPA Repository
```
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:couchdb/stable
sudo apt-get update
```

Installing CouchDB
```
sudo apt-get install couchdb
```

Ownership changes (recommended to fix the permission)

```
sudo chown -R couchdb:couchdb /usr/bin/couchdb /etc/couchdb /usr/share/couchdb
```

Once this is completed we need to fix the permissions

```
sudo chmod -R 0770 /usr/bin/couchdb /etc/couchdb /usr/share/couchdb
```

Restarting CouchDB

```
sudo systemctl restart couchdb
```

couchDB can now be accessed from http://127.0.0.1:5984/_utils/

4) Now you need to install NLTK dependencies.

```
>>> import nltk
>>> nltk.download()
```
The minimum installation requires to download the *stopwords* corpora. (Feel free to add more if you feel so)

### From pip

Coming Soon

Usage
======

## Dataset generation

The module includes a possibility to generate a dataset for raw entity words.
Example command looks as this if using source

```
python dataset_pseudo_generator.py -m en_core_web_lg -s cocaine,heroin
```

If using the package is installed 
```
from fastent import dataset_pseudo_generator

model = dataset_pseudo_generator.spacy_initialize(model_name)
dataset_pseudo_generator.dataset_generate(model,['cocaine', 'heroin'], 100)

```





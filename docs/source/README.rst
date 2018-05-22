fastent
=======

Fastent is a tool designed for creating end to end Custom Named Entity
Recognition models. Entities **ARE NOT** limited to the usual predefiend
classes of Person(PER), Location(LOC),
Companies/agencies/institutions(ORG) etc etc. Any custom entity that can
be described using a list of words can be created.

The package is comprised of several modules that can be used both
sperately for their designated tasks (i.e Anotation, contextualization,
etc etc.) or in a combined workflow. Most of the modules offer
multilingual support, meaning the datasets and text don't necessarily
require English language.

Table of contents
=================

.. raw:: html

   <!--ts-->

-  `Installation <#installation>`__
-  `Usage <#usage>`__

   -  `Dataset generation <#Dataset-Generation>`__
   -  `Contextualization <#Contextualization>`__
   -  `Api for model download <#Api>`__
   -  `Annotation <#Annotation>`__
   -  `Text utilities <#Text-utilities>`__
   -  `wordnet utilities <#Wordnet>`__
   -  `Poincare embeddings wrapper <#Poincare>`__
   -  `Combinging everyting <#combo>`__

-  `Baselines <#tests>`__
-  `Dependency <#dependency>`__

Installation
============

This section show the process for installing the package with different
methods

From source
~~~~~~~~~~~

1) lets start by cloning the package

::

    git clone https://github.com/fastent/fastent.git

2) Installing all the relevant packages

::

    pip install -r requirements.txt 

3) Install couchDB

Update the current packages

::

    sudo apt-get update

Adding PPA Repository

::

    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:couchdb/stable
    sudo apt-get update

Installing CouchDB

::

    sudo apt-get install couchdb

Ownership changes (recommended to fix the permission)

::

    sudo chown -R couchdb:couchdb /usr/bin/couchdb /etc/couchdb /usr/share/couchdb

Once this is completed we need to fix the permissions

::

    sudo chmod -R 0770 /usr/bin/couchdb /etc/couchdb /usr/share/couchdb

Restarting CouchDB

::

    sudo systemctl restart couchdb

couchDB can now be accessed from http://127.0.0.1:5984/\_utils/

4) Now you need to install NLTK dependencies.

::

    >>> import nltk
    >>> nltk.download()

The minimum installation requires to download the *stopwords* corpora.
(Feel free to add more if you feel so)

From pip
~~~~~~~~

Coming Soon

Usage
=====

Dataset generation
~~~~~~~~~~~~~~~~~~

The module includes a possibility to generate a dataset for raw entity
words. Example command looks as this if using source

::

    python dataset_pseudo_generator.py -m en_core_web_lg -s cocaine,heroin

If using the package is installed

::

    from fastent import dataset_pseudo_generator

    model = dataset_pseudo_generator.spacy_initialize(model_name)
    dataset_pseudo_generator.dataset_generate(model,['cocaine', 'heroin'], 100)


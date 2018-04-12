import subprocess
import sys
import os
import re
import json
import time
import argparse
from fast_utils import exact_word_match




class DownloadError(Exception):
    def __init__(self, output):
        self.output = output

def spacy_model_download(model_name, timeout = None):
    try :

        if sys.version_info <=(3,4):

            arguments = [python_exec, "-m",'spacy','download',model_name]
            process = subprocess.call(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output_cont = process.stdout.decode("ISO-8859-1", "ignore")

            if not exact_word_match('Successfully',output_cont):
                raise DownloadError(process.stdout.decode("ISO-8859-1", "ignore"))
            else:
                return filename.group(1)

        else:

            arguments = [python_exec(), '-m','spacy','download', model_name]
            print("Dowload for model {} stared".format(model_name))
            process = subprocess.run(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
            output_cont = process.stdout.decode("ISO-8859-1", "ignore")
            print("Dowload for model {} ended".format(model_name))

            if not exact_word_match('Successfully',output_cont):
                raise DownloadError(process.stdout.decode("ISO-8859-1", "ignore"))
            else:
                return filename.group(1)

    except (DownloadError, Exception) as e:
        print(e)

def python_exec():
    if sys.version_info <(3,):
        return 'python'

    return 'python3'


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Example with long option names')
    parser.add_argument('-l', action="store", dest = 'location', help = 'Location of the model, i.e gensim, spacy etc etc')
    parser.add_argument('-m', action="store", type=str, dest = 'model_name', help ='designated model name')
    parser.add_argument('-t', action="store", type=str, dest = 'timeout', help ='timeout', default = None)

    results = parser.parse_args()
    print(results)

    if 'spacy' in results.location:
        spacy_model_download(results.model_name, results.timeout)

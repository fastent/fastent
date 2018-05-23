import subprocess
import sys
import argparse
import requests
import shutil
import lxml.html as LH
import pandas as pd
import urllib.request
from .fast_utils import exact_word_match


class DownloadError(Exception):
    def __init__(self, output):
        self.output = output

def spacy_model_download(model_name, timeout = None):
    """
    Downloads a spacy model with name

    Args:
        model_name (str): The model name for download
    Returns:
         (void) : download in the designated folder of fastent
    """
    try :

        if sys.version_info <=(3,4):

            arguments = [python_exec, "-m",'spacy','download',model_name]
            subprocess.call(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # process = subprocess.call(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #
            # output_cont = process.stdout.decode("ISO-8859-1", "ignore")
            #
            # if not exact_word_match('Successfully',output_cont):
            #     raise DownloadError(process.stdout.decode("ISO-8859-1", "ignore"))
            # else:
            #     return filename.group(1)

        else:

            arguments = [python_exec(), '-m','spacy','download', model_name]
            print("Dowload for model {} started".format(model_name))
            process = subprocess.run(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
            output_cont = process.stdout.decode("ISO-8859-1", "ignore")
            print("Dowload for model {} ended".format(model_name))

            if not exact_word_match('Successfully',output_cont):
                raise DownloadError(process.stdout.decode("ISO-8859-1", "ignore"))
            else:
                return output_cont

    except (DownloadError, Exception) as e:
        print(e)


def fasttext_list():
    """
    Return a Dictionary of the possible fasttext models

    Args:
        None:
    Returns:
         diction_frac(dict) : Language to Model dictionary
    """

    diction_frac = {}
    try:
        content = requests.get("https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md").content
        webpage = LH.fromstring(content)
        allRefs = webpage.xpath('//a/@href')

        allRefs = [i for i in allRefs if 'amazonaws' in i and not 'zip' in i]
        allRefs

        df = pd.read_html(content)
        df = df[-1]

        assert(len(allRefs) ==  len(df['Unnamed: 0']) + len(df['Unnamed: 1'])+len(df['Unnamed: 2']))

        for i in range(len(allRefs)):
            if i%3 == 0:
                diction_frac[df['Unnamed: 0'][int(i/3)]] = allRefs[i]
            if i%3 == 1:
                diction_frac[df['Unnamed: 1'][int(i/3)]] = allRefs[i]
            if i%3 == 2:
                diction_frac[df['Unnamed: 2'][int(i/3)]] = allRefs[i]


    except Exception as e:
        print(e)
        return None

    return diction_frac

def fasttext_dowload(language_name, timeout = None):
    """
    Downloads a fasttext model with language name

    Args:
        language_name (str): The language name for download
    Returns:
         (void) : download in the designated language model to fastent folder
    """
    try:
        full_lang_dict = fasttext_list()
        url = ''
        for key in full_lang_dict:
            if language_name.lower() in key.lower():
                url = full_lang_dict[key]
                file_name = url.split('/')[-1]

        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    except Exception as e:
        print(e)



def python_exec():
    if sys.version_info <(3,):
        return 'python'

    return 'python3'


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='API options')
    parser.add_argument('-l', action="store", dest = 'location', help = 'Location of the model, i.e gensim, spacy, fastText etc etc')
    parser.add_argument('-m', action="store", type=str, dest = 'model_name', help ='designated model name')
    parser.add_argument('-t', action="store", type=str, dest = 'timeout', help ='timeout', default = None)

    results = parser.parse_args()
    print(results)

    if 'spacy' in results.location.lower():
        spacy_model_download(results.model_name, results.timeout)
    if 'fasttext' in results.location.lower():
        fasttext_dowload(results.model_name, results.timeout)

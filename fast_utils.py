import os
import time
from itertools import groupby
import re
import traceback



def log_to_text(full_metadata_list, file_name):
	try:
		if not (os.path.isfile(file_name + ".txt")):
			file=open(file_name + ".txt", "w+", encoding='utf-8', errors="surrogateescape")
			append_string = str(full_metadata_list)
			file.write(append_string)
			file.close()
		else:
			file=open(file_name + ".txt", "a+", encoding='utf-8', errors="surrogateescape")
			append_string = str(full_metadata_list)
			file.write(append_string)

	except IOError as e:
		print(e)
		print(1)

def getopts(argv):
	opts = {}  # Empty dictionary to store key-value pairs.
	while argv:  # While there are arguments left to parse...
		if argv[0][0] == '-':  # Found a "-name value" pair.
			opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
		argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.

	return opts

def remove_special_symbols(value):
	new_value =[]
	keep_char_list = ['@','.',',','!']
	for string in value:
		new_string = ''.join(e for e in string if (e.isalnum() or e in [x for x in keep_char_list]))
		if new_string:
			new_value.append(new_string)

	return new_value


def flatten(chunkList):
	sentences_split = []
	for chunk in chunkList:
		for word in chunk:
			sentences_split.append(word)
	return sentences_split


def split_with_indices(s, c=' '):
	p = 0
	for k, g in groupby(s, lambda x:x==c):
		q = p + sum(1 for i in g)
		if not k:
			yield p, q # or p, q-1 if you are really sure you want that
		p = q

def list_segmentor(seq, size):
	newseq = []
	splitsize = 1.0/max(1,size)*len(seq)
	for i in range(size):
			newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
	return newseq

def exact_word_match(word, raw_sentence):
	lister = []
	try:
		regexp_pattern = r"(?:^|\W)" + word + r"(?:$|\W)"
		#regexp_verify = re.compile(regexp_pattern) #no Need to save
		lister = re.findall(regexp_pattern, raw_sentence, flags=re.IGNORECASE)
	except Exception as e:
		print(str(traceback.format_exc()))
		return False
	return len(lister)>=1



def replace_all(text, dic):
	for i, j in dic.items():
		text = text.replace(i, j)
	return text

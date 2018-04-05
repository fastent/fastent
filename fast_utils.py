import os
from sys import argv
from itertools import groupby

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
            yield p, q-1 # or p, q if you are really sure you want that
        p = q

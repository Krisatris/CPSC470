'''
Class: CPSC475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: nlpUtils.py
The utility functions used in proj3-1.py
To Execute: don't execute this it won't work :)
'''

import itertools
import string

def get_data(fname):
    fin = open(fname, 'r')
    line_list = fin.readlines()
    return line_list

def tokenize(text_lst):
    result_lst = []

    for i in text_lst:
        finished_line = '<s>' + i
        finished_line = finished_line.replace('\n', '</s>')
        finished_line = ''.join(j if ord(j) < 128 else '' for j in finished_line)

        result_lst.append(finished_line)

    return result_lst

def make_grams(sent_list, gram_size):
    ngrams_list = []
    for line in sent_list:
        linegrams_list = []
        words = line.split()
        for index, word in enumerate(words):
            if(index <= len(words)-gram_size):
                if(gram_size == 1):
                    ngram = word
                if(gram_size == 2):
                    ngram = word + ' ' + words[index + 1]
                if(gram_size == 3):
                    ngram = word + ' ' + words[index + 1] + ' ' + words[index + 2]
                if(gram_size == 4):
                    ngram = word + ' ' + words[index + 1] + ' ' + words[index + 2] + ' ' + words[index + 3]
                linegrams_list.append(ngram)
        ngrams_list.append(linegrams_list)
    merged_list = list(itertools.chain.from_iterable(ngrams_list))
    return merged_list

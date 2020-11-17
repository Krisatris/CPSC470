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
from random import random
from random import randint
import numpy as np

def make_choice(objects, weight):
    rand = random()
    for wtIdx in range(len(weight)):
        if rand < weight[wtIdx]:
            return objects[wtIdx]

def get_data(fname):
    fin = open(fname, 'r')
    line_list = fin.readlines()
    return line_list

def tokenize(text_lst):
    result_lst = []

    for i in text_lst:
        finished_line = '<s> ' + i
        finished_line = finished_line.replace('\n', ' </s>')
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

def count_grams(gram_list):
    temp_dict = dict()
    for item in gram_list:
        if item in temp_dict:
            temp_dict[item] += 1
        else:
            temp_dict[item] = 1
    {k: v for k, v in sorted(temp_dict.items(), key = lambda item: item[1])}
    gram_words = list(temp_dict.keys())
    gram_nums = list(temp_dict.values())
    weights = np.array(gram_nums, dtype=np.float64)
    sum_of_weights = weights.sum()
    np.multiply(weights, 1/sum_of_weights, weights)
    weights = weights.cumsum()
    return gram_words, weights

def make_lines(gram_words, gram_nums, gram_size):
    output = []
    for i in range(5):
        line = []
        rand = randint(0, len(gram_words))
        while '<s>' not in gram_words[rand]:
            rand = randint(0, len(gram_words))
        temp = gram_words[rand]
        temp = temp[4:]
        line.append(temp)
        i = 0
        while i < (10 // gram_size):
            temp = make_choice(gram_words, gram_nums)
            if '<s>' not in temp and '</s>' not in temp:
                line.append(temp)
                i += 1
        rand = randint(0, len(gram_words))
        while '</s>' not in gram_words[rand]:
            rand = randint(0, len(gram_words))
        temp = gram_words[rand]
        temp = temp[:(len(temp) - 4)]
        line.append(temp)
        output.append(line)
    return output

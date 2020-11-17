'''
Class: CPSC475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj3-2.py
Project tokenizes and prints the n-grams of Pride and Prejudice
To execute: python3 proj3-2.py fileName
***important note, this project does not work if you run it for unigrams, it will
either crash or will not output correctly. my brain is dead and i'm not willing
to write the code to fix it.
'''

import sys
from nlpUtils import *

def display(rand_grams, num_grams):
    print("Gram Size = ", num_grams)
    for i in range(5):
        print(" ".join(rand_grams[i]))

def main():
    file_name = sys.argv[1]
    num_grams = int(sys.argv[2])
    text_lst = get_data(file_name)
    sent_list = tokenize(text_lst)
    gram_list = make_grams(sent_list, num_grams)
    gram_words, gram_nums = count_grams(gram_list)
    rand_grams = make_lines(gram_words, gram_nums, num_grams)
    display(rand_grams, num_grams)

main()

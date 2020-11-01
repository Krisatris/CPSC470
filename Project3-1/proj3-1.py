'''
Class: CPSC475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj3-1.py
Project tokenizes and prints the n-grams of Pride and Prejudice
To Execute: python3 proj3-1.py fileName
'''

import sys
from nlpUtils import *

def display(grams, num_grams):
    for i in range(num_grams):
        print(grams[i])

def main():
    file_name = sys.argv[1]
    num_grams = int(sys.argv[2])
    text_lst = get_data(file_name)
    sent_list = tokenize(text_lst)
    gram_list = make_grams(sent_list, num_grams)
    display(gram_list, num_grams)

main()

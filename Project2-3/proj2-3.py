'''
Class: CPSC 475
Team Member 1: Stella Beemer
Team Member 2: None
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj2-3.py
Project uses Zipf's law the analyze the frequency of words in a spoken-word corpus
All four files look equally zipfian as they visually have a near identical slope
To Execute: python3 proj2-3.py directory tokenizerNum
'''

from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import string
from porter import PorterStemmer

'''
pre:  dictionary is a sorted list of words in a text and the frequency they occur in
post: plots the graph of how often the words occur
'''
def plot(dictionary):
    x = range(1, len(dictionary) + 1)
    y = np.array(list(dictionary.values()))
    plt.plot(np.log(x), np.log(y))
    plt.show()

'''
pre:  wordList is an ordered list of all the words in user-inputted file
post: dictionary is a key-value pair collection of each word in the file and
      the frequency at which it ocurrs, sorted by frequency
'''
def count(wordList):
    dictionary = dict()
    for w in wordList:
        if w in dictionary:
            dictionary[w] = dictionary[w] + 1
        else:
            dictionary[w] = 1
    sortedDictionary = {j: i for j, i in sorted(dictionary.items(),
                                                key=lambda x: x[1], reverse=True)}
    return sortedDictionary

'''
pre:  text is a string containing all of the text in a user-entered file
post: returns a list of all the words in text split using a tokenizer/
      normalizer similar to the one in ex15
'''
def customToken(text):
    dict = {ord(ch) : ch for ch in text if ord(ch) > 127}
    nonAscii = ''.join(list(dict.values()))

    wordList = text.split()
    remove = string.digits + string.punctuation + nonAscii
    table = str.maketrans('', '', remove)
    wordList = [w.translate(table) for w in wordList]
    wordList = [word for word in wordList if len(word) > 0]
    wordList = [word.lower() for word in wordList]
    wordList = [word for word in wordList if len(word) > 1 or word == 'i'
                or word == 'a']
    return wordList

'''
pre:  text is a string containing all of the text in a user-entered file
post: returns a list of all the words in text split using the Porter normalizer
'''
def porter(text):
    p = PorterStemmer()
    output = ''
    word = ''
    line = text.split('\n')
    for c in line:
        if c.isalpha():
            word += c.lower()
        else:
            if word:
                output += p.stem(word, 0, len(word) - 1)
                word = ''
            output += c.lower()
    return output.split()

'''
pre:  text is a string containing all of the text a user-entered file
post: returns a list of all the words in text split by their white spaces
'''
def spaceToken(text):
    return text.split()

'''
pre:  fname is the file name of a textfile entered by the user
post: all of the text in the user entered file is imported into a string
'''
def getData(dName):
    directoryList = os.listdir(dName)
    text = ""
    os.chdir(dName)
    for file in directoryList:
        fin = open(file, 'r')
        text = text + " " + fin.read()
        fin.close()
    os.chdir("..")
    fout = open("BSC.txt", 'w')
    fout.write(text)
    fout.close()
    return text

'''
pre:  main function, called at end of program
post: calls the functions to tokenize/normalize and analyze program
'''
def main():

    directoryName = sys.argv[1]
    tokenizer = sys.argv[2]

    text = getData(directoryName)

    if (tokenizer == '1'):
        wordList = spaceToken(text)
    elif(tokenizer == '2'):
        wordList = word_tokenize(text)
    elif(tokenizer == '3'):
        wordList = porter(text)
    elif(tokenizer == '4'):
        wordList = customToken(text)

    dictionary = count(wordList)

    plot(dictionary)


main()

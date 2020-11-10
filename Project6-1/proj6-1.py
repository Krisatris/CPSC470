'''
Class: CPSC 475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj6-1.py
To Execute: python3 proj6-1.py
'''

import sys
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

def tfidf(textList, ngrams):
    #get ngrams
    vectorizer = CountVectorizer(ngram_range = (ngrams, ngrams))
    X1 = vectorizer.fit_transform(textList)
    features = (vectorizer.get_feature_names())

    #apply tfidf
    vectorizer = TfidfVectorizer(ngram_range = (ngrams, ngrams))
    X2 = vectorizer.fit_transform(textList)
    scores = (X2.toarray())

    sums = X2.sum(axis = 0)
    data1 = []
    for col, term in enumerate(features):
        data1.append((term, sums[0, col]))
    ranking = pd.DataFrame(data1, columns = ['term', 'rank'])
    words = (ranking.sort_values('rank', ascending = False))
    print("\n\nWords head: \n", words.head(20))

def normalize(textList):
    resultList = []
    for i in textList:
        finishedLine = i
        finishedLine = finishedLine.replace('\n', '')
        finishedLine = ''.join(j if ord(j) < 128 else '' for j in finishedLine)
        if not(finishedLine.isdecimal()):
            resultList.append(finishedLine)
    return resultList

def main():
    ngrams = int(sys.argv[1])
    fin = open("brick.txt", 'r')
    lineList = fin.readlines()
    normalized = normalize(lineList)
    tfidfList = tfidf(normalized, ngrams)

main()

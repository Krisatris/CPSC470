'''
Class: CPSC475
Team Member 1: Stella Beemer
Submitted By: Stella Beemer
GU Username: sbeemer2
File name: proj4-1.py
To execute: python3 proj4-1.py
'''

import nltk
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk import word_tokenize
import random
import string

def writeData(fname, data):
    fout = open(fname, 'w')
    fout.write(' '.join(data))
    fout.close

def getWords(files):
    return [word for fname in files for word in tokenize(movie_reviews.words(fname))]

def tokenize(review):
    review = ' '.join(review)
    tokenizedReview = word_tokenize(review)
    stopWords = set(stopwords.words('english'))
    return [word for word in tokenizedReview if word not in stopWords]

def getFiles(idType):
    files = movie_reviews.fileids(idType)
    testFiles = []
    for i in range(0, 10):
        index = random.randrange(0, len(files))
        testFiles.append(files[index])
        del files[index]

    return files, testFiles

def main():

    posReviews, testPosReviews = getFiles('pos')
    negReviews, testNegReviews = getFiles('neg')

    posWords = getWords(posReviews)
    posTestWords = getWords(testPosReviews)

    negWords = getWords(negReviews)
    negTestWords = getWords(testNegReviews)

    writeData('pos.txt', posWords)
    writeData('postTst.txt', posTestWords)

    writeData('neg.txt', negWords)
    writeData('negTst.txt', negTestWords)

main()

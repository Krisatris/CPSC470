'''
Class: CPSC 475
Team Member 1: Stella Beemer
Submitted by: Stella Beemer
GU Username: sbeemer2
File name: proj6-1.py
To Execute: python3 proj6-1.py ngrams
'''

import nlpUtils as nlp
import nltk
import pandas as pd
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cdist
from scipy.stats import zscore
from sklearn import preprocessing
import sys

def createDeleteWords():
    deletewords = []
    deletewords = stopwords.words('english')
    deletewords.append('<s>')
    deletewords.append('</s>')
    deletewords.append('and')
    deletewords.append('to')
    deletewords.append('the')
    return deletewords

def vocabLemmatization(data, deleteWords):
    newData = []
    vocab = []
    for sentence in data:
        newSentence = ''
        sentence = sentence.split()
        for word in sentence:
            if word not in deleteWords:
                word = nlp.lemmatize(word)
                vocab.append(word[:-1])
                newSentence = newSentence + word
        newData.append(newSentence)
    vocab = list(set(vocab))
    return vocab, newData

def tfidf_vector(doc1, doc2):
    doc1 = ' '.join(doc1)
    doc2 = ' '.join(doc2)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([doc1, doc2])
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    return df

def makeFinalDict(words, vocab, grams):
    finalDict = {}
    for word in words:
        for i in vocab:
            finalDict[word] = {}
    for word in words:
        for i in vocab:
            finalDict[word][i] = 0

    for gram in grams:
        gram = gram.split()
        for word in gram:
            if word in words:
                for i in vocab:
                    if i in gram:
                        finalDict[word][i] = finalDict[word][i] + 1
    return finalDict

def vectorize(words, vocab, finalDict):
    vectorDict = []
    for word in words:
        vector = []
        for i in vocab:
            vector.append(finalDict[word][i])
        vectorDict.append(vector)
    return vectorDict

def main():
    data = nlp.tokenize(nlp.getData('brick.txt'))
    doc1 = data[:int(len(data)/2)]
    doc2 = data[int(len(data)/2):]
    deleteWords = createDeleteWords()
    vocab1, doc1 = vocabLemmatization(doc1, deleteWords)
    vocab2, doc2 = vocabLemmatization(doc2, deleteWords)
    newData = doc1 + doc2
    vocab = set(vocab1 + vocab2)
    df1 = tfidf_vector(doc1, doc2)
    df1 = df1[df1 > 0]
    df1.dropna(axis = 1, inplace = True)
    words = df1.sum().sort_values(ascending = False).head(60).index
    grams = nlp.makeNgram(newData, 7)
    finalDict = makeFinalDict(words, vocab, grams)
    vectorDict = vectorize(words, vocab, finalDict)
    distances = cdist(vectorDict, vectorDict, metric='euclidean')
    df = pd.DataFrame(data = distances, index = words, columns = words)
    x = df.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled, index = words, columns = words)

    print(df['the']['pin'])
    print(df['think']['back'])
    print(df['said']['dode'])
    print(df['dode']['pin'])
    print(df['you']['think'])
    print(df['tug']['pin'])
    print(df['he']['said'])
    print(df['pin']['alright'])
    print(df['the']['like'])
    print(df['think']['like'])

main()

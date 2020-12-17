'''
Class: CPSC 475-01
Submitted By: Sami Blevens
GU Username: sblevens
File Name: proj4-1.py
Program illustrates: 
To build & execute: python3 proj4-1.py
'''

import nltk
import string
import math
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

def main():
   logPrior, likelihoods, vocab, test_list = train()
   test_list = [item for sublist in test_list for item in sublist]
   for title in test_list:
      review = movie_reviews.words(title)  #list of words in a review
      review = ' '.join(review)  #make into string to tokenize
      tok = word_tokenize(review) #tokenize returns a list

      remove = string.digits + string.punctuation
      table = str.maketrans('','',remove)
      filtered = [w.translate(table) for w in tok]

      stop_words = set(stopwords.words('english')) #common small words
      filtered = [w for w in filtered if w not in stop_words] #stop words removed

      filtered = [w for w in filtered if len(w)>0]

      text = ' '.join(filtered)


      argmax = test(text,logPrior,likelihoods,vocab)
      print(title)
      if(argmax == 0):
         print("argmax is 0")
      if(argmax == 1):
         print("argmax is 1")



def train():
   print('train')
   test_list = []
   logPrior = []
   likelihoods = {}
   big_doc = []
   N_docs = len(movie_reviews.fileids())
   #vocab = []
   #for fileid in movie_reviews.fileids():
      #  vocab.append(set(w.lower() for w in movie_reviews.words(fileids)))
   classes = movie_reviews.categories()
   vocab = []
   text_c = ''
   c_id=0
   for c in classes:
      likelihoods[c_id] = {}
      class_list = movie_reviews.fileids(c)
      N_c = len(class_list)
      logPrior.append(math.log(N_c/N_docs))

      #get test and train list
      tenPercent = int(len(class_list)*.1)
      lastPercent = int(len(class_list)*.9)
      testList = class_list[:tenPercent]
      class_List = class_list[-lastPercent:]
      test_list.append(testList)
      
      #put all c docs into big doc [c]
      
      
      for title in class_list:
         review = movie_reviews.words(title)  #list of words in a review
         review = ' '.join(review)  #make into string to tokenize
         tok = word_tokenize(review) #tokenize returns a list

         remove = string.digits + string.punctuation
         table = str.maketrans('','',remove)
         filtered = [w.translate(table) for w in tok]

         stop_words = set(stopwords.words('english')) #common small words
         filtered = [w for w in filtered if w not in stop_words] #stop words removed

         filtered = [w for w in filtered if len(w)>0]

         text = ' '.join(filtered)
         #get vocab
         for w in filtered:
            vocab.append(w)

         #print("text " + text)
         text_c = text_c + text + " "
         #print(text_c)

   
      vocab = list(dict.fromkeys(vocab))
      big_doc.append(text_c)
      c_id = c_id + 1


   #restart the loop, because needed vocab from both classes
   c_id = 0
   for c in classes:
      print(c)
      count_w_v_c = 0
      for w in vocab:
         count_w_v_c = big_doc[c_id].count(w) + 1 + count_w_v_c
      for w in vocab:
         count_w_c = big_doc[c_id].count(w) + 1
         likelihoods[c_id][w] = math.log(count_w_c/count_w_v_c)
      c_id = c_id + 1  

   return logPrior, likelihoods, vocab, test_list


def test(text,logPrior,likelihoods,vocab):
   print("testing")
   print(str(len(logPrior)) + " " + str(logPrior[0]) + " " str(logPrior[1]))

   classes = movie_reviews.categories()
   sums = []
   c_id = 0
   for c in classes:
      print(c)
      sums.append(logPrior[c_id])
      i = 0
      for i_word in text:
         word = text[i]
         if word in vocab:
            sums[c_id] = sums[c_id] + likelihoods[c_id][word]
         i = i + 1
      c_id = c_id + 1
   
   print(str(sums[0]) + " vs " + str(sums[1]))
   return np.argmax(sums,axis = 0)


main()


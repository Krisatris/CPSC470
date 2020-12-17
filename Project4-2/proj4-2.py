'''
Class: CPSC 475-01
Team Member 1: Stella Beemer
Team Member 2: Sami Blevens
Submitted By: Stella Beemer
GU Username: sbeemer2
File Name: proj4-2.py
Program illustrates: generating data for naive bayes text classfication
To build & execute: python3 proj4-2.py
'''
import nltk
import string
import numpy as np
import math
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

def main():
   pos_text = open("pos.txt","w")
   pos_test_text = open("posTst.txt","w")
   neg_text = open("neg.txt","w")
   neg_test_text = open("negTst.txt","w")

   pos_list = movie_reviews.fileids('pos')
   neg_list = movie_reviews.fileids('neg')

   #separate 10%
   pos_List, posTestList = gen_test(pos_list,pos_test_text)
   neg_List, negTestList = gen_test(neg_list,neg_test_text)

   #generate words
   pos_words = gen_words(pos_List,pos_text)
   neg_words = gen_words(neg_List, neg_text)

   #generate vocab
   vocab = get_vocab(pos_words, neg_words)
   logPrior, likelihoods = train(vocab, pos_words, neg_words)

   #test the naive
   negCount = 0
   posCount = 0
   test_titles = negTestList + posTestList
   for title in test_titles:
      print(title)
      testdoc = movie_reviews.words(title)
      argmax = test(testdoc, logPrior, likelihoods, vocab)
      print(argmax)
      if('neg' in title and argmax == 0):
         negCount += 1
      elif('pos' in title and argmax == 1):
         posCount += 1

   #print accuracies
   negAccuracy = (negCount / len(negTestList)) * 100
   print("negative accuracy = %" + str(negAccuracy))
   posAccuracy = (posCount / len(posTestList)) * 100
   print("positive accuracy = %" + str(posAccuracy))
   totalAccuracy = ((negCount + posCount) / len(test_titles)) * 100
   print("total accuracy = %" + str(totalAccuracy))

'''
Pre: send in two lists, pos_words and neg_words
Post: returns list of all vocab words in both lists
'''
def get_vocab(pos_words, neg_words):
   vocab = []
   words = pos_words + neg_words
   for w in words:
      vocab.append(w)

   vocab = list(dict.fromkeys(vocab))
   return vocab

'''
Pre: send in vocab, pos_words, and neg_words lists
Post: returns the priors and likelihoods
'''
def train(vocab, pos_words, neg_words):
   n_doc = len(movie_reviews.fileids())
   logPrior = []
   likelihoods = {}
   big_doc = [neg_words, pos_words]
   classes = movie_reviews.categories()
   c_id = 0

   for c_id, c in enumerate(classes):
      n_c = len(movie_reviews.fileids(c))
      likelihoods[c_id] = {}
      
      logPrior.append(math.log(n_c/n_doc))

      vocab_c = list(dict.fromkeys(big_doc[c_id]))
      ct_vocab_c = len(vocab_c)

      #calc P(w|c)
      for w in vocab:
         ct_w_c = big_doc[c_id].count(w)
         likelihoods[c_id][w] = math.log((ct_w_c + 1)/(ct_vocab_c + 1))
      print(c + " is finished in train")

   return logPrior, likelihoods


'''
Pre: send in the words to be tested, priors, likelihoods, and vocab of dataset
Post: returns index of class that has the higher likelihood (0 or 1)
'''
def test(testdoc, logPrior, likelihoods, vocab):
   classes = movie_reviews.categories()
   sums = []

   for c_id, c in enumerate(classes):
      sums.append(logPrior[c_id])
      for i, word in enumerate(testdoc):
         word = testdoc[i]
         if word in vocab:
            sums[c_id] = sums[c_id] + likelihoods[c_id][word]

   print(str(sums[0]) + " vs " + str(sums[1]))
   return np.argmax(sums)
   
'''
Pre: send in the list of titles and the file to output the test files 
Post: separates the first 10% and last 90% of titles, writes test files to output
      and returns rest of 90% titles
'''
def gen_test(title_list,fout):
   tenPercent = int(len(title_list)*.1)
   lastPercent = int(len(title_list)*.9)
   test_List = title_list[:tenPercent]
   title_List = title_list[-lastPercent:]

   fout.writelines("%s\n" % title for title in test_List)

   return title_List, test_List

'''
Pre: send in the list of titles and the file to ouput the words generated
Post: generates list of words and writes them to the outfile
'''
def gen_words(title_list,fout):
   words = []
   for title in title_list:
      review = movie_reviews.words(title)  #list of words in a review
      review = ' '.join(review)  #make into string to tokenize
      tok = word_tokenize(review) #tokenize returns a list

      remove = string.digits + string.punctuation
      table = str.maketrans('','',remove)
      filtered = [w.translate(table) for w in tok]

      stop_words = set(stopwords.words('english')) #common small words
      filtered = [w for w in filtered if w not in stop_words] #stop words removed

      filtered = [w for w in filtered if len(w)>0]

      words.append(filtered)

   words = [item for sublist in words for item in sublist]

   fout.writelines("%s\n" % word for word in words)

   return words

main()

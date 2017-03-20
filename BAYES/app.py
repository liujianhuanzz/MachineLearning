import bayes
from numpy import *

listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print myVocabList
print bayes.setOfWords2Vec(myVocabList, listOPosts[3])

bayes.spamTest()

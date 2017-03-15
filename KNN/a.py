import kNN

group, labels = kNN.createDataSet()

result = kNN.classify([0, 0], group, labels, 3)
print (result)
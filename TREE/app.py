import trees
import treePlotter

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesTree = trees.createTree(lenses, lensesLabels[:])
print trees.classify(lensesTree, lensesLabels, ['young', 'hyper','no','normal'])
print trees.classify(lensesTree, lensesLabels, ['presbyopic', 'myope','no','normal'])
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

# this program is based on the iris dataset. It removes three(3) entries
# from the dataset for testing purposes. It prints the testing targets.
# Then it prints the prediction for the targets. They match !
# Then, the programm creates a PDF document where we can see
# the actual decision tree.
# Finally, we print datas from the test case and follow
# the decision tree to see what kind of flower it is
# Fascinating !!!
# requirements : Pydotplus and graphviz installed.

# load dataset
iris = load_iris()

# print some informations from the dataset
# print iris.feature_names
# print iris.target_names
# print iris.data[0]
# print iris.target[0] 0=setosa ; 1=versicolor ; 2=virginica

# testing data
testIndex = [0, 50, 100]
testingTarget = iris.target[testIndex]
testingData = iris.data[testIndex]

# training data
trainingTarget = np.delete(iris.target, testIndex)
trainingData = np.delete(iris.data, testIndex, axis = 0)

# the Classifier
classifier = tree.DecisionTreeClassifier()
# training the Classifier
classifier.fit(trainingData, trainingTarget)

print testingTarget
print classifier.predict(testingData)

# visualisation script

from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()

tree.export_graphviz(classifier,
				out_file = dot_data,
				feature_names=iris.feature_names,
				class_names=iris.target_names,
				filled=True, rounded=True,
				impurity=False)
graph= pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")


# Here we want to navigate the decision tree
# so we print the test data with the features and the answer-label
print testingData[2], testingTarget[2]

#this will give us details of the features + names of flower for the labels
print iris.feature_names, iris.target_names

# (Source : YouTube - google developpers - Josh Gordon)




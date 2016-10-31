#import sklearn # you have to check if there is no import error first ! (scikit-learn installed)

from sklearn import tree

# This programm detect if a fruit is an apple(0) or an orange(1)

# Collecting training data
# 2 Features : weigth in grams and texture: 0-bumpy 1-smooth
# 2 Labels : 0-apple 1-orange

features = [[140, 1], [130, 1], [150, 0], [170, 0]]

labels = [0,0,1,1]

# the Classifier
classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(features, labels)# fit = finds patterns in data

print classifier.predict([[160,0]]) # 160 grams AND bumpy

# answer will be [1] for orange !

#Source : youtube - google developpers - Josh Gordon


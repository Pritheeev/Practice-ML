#This is just a very basic hello world ML program
from sklearn import tree
#The first attribute says the weight and the second one says if it is bumpy or smooth
#1- smooth, 0- bumpy
features=[[140,1],[130,1],[150,0],[170,0]]
#0- apple, 1- orange
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
x,y= int(raw_input("Enter the attributes of the fruit (the fruit's weight in grams and its texture i.e 1 if its smooth and 0 if its bumpy)"))
print("The fruit must be :"),
print clf.predict([x,y])

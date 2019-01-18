from sklearn import tree

#Gender classifier withw height and weight 
#training data with two attributes height and weight 

X = [[177,80],[180,80],[150,50],[190,90],[143,40],[149,35],[180,75],[166,60]]

Y = ["Male","Male","Female","Male","Female","Female","Male","Female"]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[178,78]])

print (prediction)


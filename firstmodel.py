from sklearn.tree import DecisionTreeClassifier
features=[[140,0],[130,0],[150,1],[170,1]] #datas r specified ,smotth 0 bumpy 1
labels=[0,0,1,1] #apple 0 mango 1

clf=DecisionTreeClassifier()
clf.fit(features,labels) #used to learn data

p=clf.predict([144,1])  #value btw 150 & 170
print("prediction=",p)


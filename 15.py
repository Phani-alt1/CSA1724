from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

X = [[0,0,0,0],[0,0,0,1],[1,0,0,0],[2,1,0,0],[2,2,1,0],
     [2,2,1,1],[1,2,1,1],[0,1,0,0],[0,2,1,0],[2,1,1,0]]
y = [0,0,1,1,1,0,1,0,1,1]

clf = DecisionTreeClassifier().fit(X, y)
print("Play Tennis?", "Yes" if clf.predict([[2,2,1,1]])[0] else "No")

plot_tree(clf, feature_names=['Outlook','Temp','Humidity','Windy'],
          class_names=['No','Yes'], filled=True)
plt.show()

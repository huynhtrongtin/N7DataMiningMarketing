# -*- coding: utf-8 -*-
"""AICayQuyetDinh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oZmXicEr47UtQr88GVL9emYh5sQ_KNSb
"""

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Load dataset
dataset = pd.read_csv("/content/FILE_DT.csv")
dataset.describe()

import seaborn as sns
sns.pairplot(dataset, x_vars=['Youtube','Facebook','TV','Radio','Newspaper'],y_vars='Sales',size=7,aspect=0.7)

dataset.corr()

cut_lables = ['Low','Medium','Hight']
cut_bins = [0,10,20,100]
dataset['Sale_label']= pd.cut(dataset['Sales'],bins=cut_bins,labels=cut_lables)
dataset

dataset.groupby('Sale_label').size()

dataset.drop('Sales',axis=1,inplace=True)
dataset

from sklearn.model_selection import train_test_split
array = dataset.values
X = array[:,0:5]
y = array[:,5]
X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=0)

from sklearn import tree
decision_tree = tree.DecisionTreeClassifier(criterion='gini')
decision_tree.fit(X_train,y_train)
predictions = decision_tree.predict(X_test)
print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

print('Accuracy of the dicision tree classifier on train data {:.2f}'.format(decision_tree.score(X_train,y_train)))
print('Accuracy of the dicision tree classifier on train data {:.2f}'.format(decision_tree.score(X_test,y_test)))

new_ads= pd.DataFrame({'Youtube':[120,35],'Facebook':[200,50],'TV':[100,50],'Radio':[25,20],'Newspaper':[20,10]})
new_ads

sale_pred= decision_tree.predict(new_ads)
sale_pred

import pandas as pd
feature_imp = pd.Series(decision_tree.feature_importances_,index=dataset.columns.values[0:5])
feature_imp

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title('Visualizing Important Features')
plt.legend()
plt.show()

feature = dataset.columns[0:5]
target = dataset['Sale_label'].unique()

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import datasets
from IPython.display import Image
import pydotplus

dot_data = tree.export_graphviz(decision_tree,out_file=None,feature_names=feature,class_names=target)

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
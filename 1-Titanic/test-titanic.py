import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;

train = pd.read_csv('train.csv');
# print(titanic_train);
test = pd.read_csv('test.csv');
test['Survived'] = 'NA';
# print(titanic_test);
# print(titanic_train[0:5]);

# now take a bar chart of each features and differentiate with the survived and unsurvived :
def bar_chart(feature) :
	survived_train = train[train['Survived']==1][feature].value_counts();
	print(train[train['Survived']==1][feature]);
	dead_train = train[train['Survived'] == 0][feature].value_counts();
	x=train[train['Survived']==1][feature];
	labels = [str(i) for i in range(1,len(survived_train)+1)];
	plt.bar(range(1,len(survived_train)+1), dead_train, tick_label=labels);
	plt.bar(range(1,len(survived_train)+1), survived_train, bottom=dead_train, tick_label=labels);
	plt.show();

bar_chart('Sex');





input("Press any key to continue... ");
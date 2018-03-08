# The goal is to apply LDA to a data set
import matplotlib.pyplot as plt # importing library for plotting
from sklearn import datasets # importing library for datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis # importing LDA 

iris = datasets.load_iris() # loading the  iris data from datasets

X = iris.data # the data from data set (predictors) with 4 attributes: sepal length, sepal width, petal length and petal width.
y = iris.target # the values on the y axis

target_names = iris.target_names # names of the flowers Setosa, Versicolour and Virginica

lda = LinearDiscriminantAnalysis(n_components=2) # setting LDA model

model = lda.fit(X, y).transform(X) # fitting the LDA model to the given data to classify the 3 flowers

colors = ['blue', 'green', 'purple'] # setting the plot colors for the graph

for color, i, target_name in zip(colors, [0, 1, 2], target_names): # printing the LDA graph with three colors and flower names
    plt.scatter(model[y == i, 0], model[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')

plt.show()
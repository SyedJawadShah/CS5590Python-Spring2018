# The goal is to download a data set and applied Support vector machine model with linear and RBF kernel.
from sklearn import datasets,metrics # importing the library for data sets
from sklearn import svm # importing the support vector machine model
from sklearn.model_selection import train_test_split # Importing the library to split the data into training and test sets

datasets1=datasets.load_breast_cancer() # The data used is for breast cancer patients
x=datasets1.data # predictor attributes
y=datasets1.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20) # spliting the data into 80% train and 20 % test
#linear kernel section
model_linear=svm.SVC(kernel='linear') # declaring the SVM model with linear kernel
y_predict = model_linear.fit(x_train,y_train).predict(x_test) # applying the linear model to the data
print('The score of the model with linear kernel applied is: ',(model_linear.score(x,y))) # Getting the score for the model
print('\n','The accuracy of the model with linear kernel is: ', metrics.accuracy_score(y_test,y_predict)) # Getting model accuracy
# RBF Kernel section
model_rbf=svm.SVC(kernel='rbf') # declaring the SVM model with RBF kernel
y_predict_rbf = model_rbf.fit(x_train,y_train).predict(x_test) # applying the rbf model to the data
print('\n','The score of the model with RBF kernel applied is: ',(model_rbf.score(x,y))) # Getting the score for the model
print('\n','The accuracy of the model with RBF kernel is: ', metrics.accuracy_score(y_test,y_predict_rbf))# Getting model accuracy

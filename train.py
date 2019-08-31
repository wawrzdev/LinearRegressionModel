#Linear Regression code adapted from the following: https://stackabuse.com/multiple-linear-regression-with-python/

#Using sklearn Boston Housing Datasheet with the following continuous linear features
#LSTAT - % lower status of the population
#TAX - full-value property-tax rate per $10,000
#RM - average number of rooms per dwelling
#ZN - proportion of residential land zoned for lots over 25,000 sq.ft.

#imports
import numpy as np
import pandas as pd
import pickle
#from sklearn.externals import joblib 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

def main():
    #PREPARE DATA
    data_set = load_boston()    #Using boston housing dataset for ease of use
    boston = pd.DataFrame(data_set.data, columns=data_set.feature_names)
    boston['MEDV'] = data_set.target

    X = pd.DataFrame(np.c_[boston['LSTAT'],boston['TAX'], boston['ZN'], boston['RM']], columns=['LSTAT','TAX','ZN','RM'])
       
    y = boston['MEDV']
        

    #CREATE MODEL
    #split dataframe into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 9)


    #TRAIN MODEL
    model = LinearRegression()
    model.fit(X_train, y_train)


    #EVALUATE MODEL
    pred = model.predict(X_test)

    test_rmse = (np.sqrt(mean_squared_error(y_test, pred)))
    test_r2 = r2_score(y_test, pred)
    print("Root mean squared error: ")
    print(test_rmse)
    print("R squared value: ")
    print(test_r2)

    #SAVE MODEL FOR FUTURE USE
    with open('trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)


main()


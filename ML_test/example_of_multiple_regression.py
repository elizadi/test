import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")        #reading data from a file

X = df[['Weight', 'Volume']]        #list of the independent values a variable
y = df['CO2']       #list of the dependent values a variable

regr = linear_model.LinearRegression()
regr.fit(X, y)      #description of the relationship between the passed parameters

# print(regr.predict([[2200, 1500]]))     #predict value y based on values X
# print(regr.coef_)       #print the coefficient values of the regression object. he value by which the dependent variable changes when one of the independent variables is increased by one
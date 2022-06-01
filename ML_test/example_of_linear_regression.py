import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

# plt.scatter(x, y) #draw the original scatter plot
# plt.plot(x, mymodel)  #draw the line of linear regression
# plt.show()    #display the diagram

# print(r)  #relationship between the values x-axis and y-axic
print(myfunc(10))   #predict for value x = 10
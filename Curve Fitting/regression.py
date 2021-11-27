import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 18})

def sortingList(x, y):
    zip_list = zip(x, y)
    sorted_list = sorted(zip_list)
    
    x = [item[0] for item in sorted_list]
    y = [item[1] for item in sorted_list]
    
    return x, y

def linearRegression(x, y):
    num1 = 0
    for i in range(len(x)):
        num1 += (x[i]*y[i])
        
    den1 = 0
    for i in range(len(x)):
        den1 += (x[i]*x[i])
    
    k2 = num1/den1
    
    return k2

def exponentialRegression(x, y):
    num1 = 0
    for i in range(len(x)):
        num1 += (x[i]*np.log(abs(y[i])))
    num1 *= len(x)
    
    s = 0
    for i in range(len(x)):
        s += np.log(abs(y[i]))
    num2 = sum(x)*s
    
    den1 = 0
    for i in range(len(x)):
        den1 += (x[i]*x[i])
    den1 *= len(x)
    
    den2 = sum(x)*sum(x)
    
    x_bar = sum(x)/len(x)
    y_bar = s/len(y)
    
    k2 = (num1 - num2)/(den1 - den2)
    k1 = y_bar - k2*x_bar
    
    return np.exp(k1)

x = []
y = []
data = open("data.txt", "r")
line = data.readline()
while line:
    l = line.split()
    x.append(float(l[0]))
    y.append(float(l[1]))
    line = data.readline()
data.close()

x, y = sortingList(x, y)

a = linearRegression(x, y)
b = exponentialRegression(x, y)

y_plot = []
for i in range(len(x)):
    y_plot.append(a*x[i] + b*np.exp(x[i]))

plt.figure(figsize = (12, 12))
plt.scatter(x, y, c='g', alpha=1)
plt.plot(x, y_plot, 'b')
plt.title('Curve Fitting/Regression')
plt.xlabel('x')
plt.ylabel('y=ax+be^x')
plt.show()




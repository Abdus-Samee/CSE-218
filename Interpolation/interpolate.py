import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def combinedValue(a, b, p, q):
    return (a-b)/(p-q)

def newtonDividedDifference(x, y, degree, val):
    table = []
    limit = degree+1
    for i in range(degree+1):
        temp = []
        for j in range(limit-i):
            #append in temp
            if i == 0:
                temp.append(y[j])
            else:
                temp.append(combinedValue(table[i-1][j+1], table[i-1][j], x[i+j], x[j]))
                
        table.append(temp)

    b = []
    for i in range(degree+1):
        b.append(table[i][0])

    prod = []
    prod.append(1)
    for i in range(1, degree+1):
        prod.append(prod[i-1]*(val-x[i-1]))

    ans = 0
    for i in range(0, degree+1):
        ans += prod[i]*b[i]

    return ans


m = []
time_mass = []
v = []
time_vel = []

massFile = open("mass.txt", "r")
myline = massFile.readline()
while myline:
    l = myline.split()
    time_mass.append(int(l[0]))
    m.append(float(l[1]))
    myline = massFile.readline()
massFile.close()

velFile = open("velocity.txt", "r")
myline = velFile.readline()
while myline:
    l = myline.split()
    time_vel.append(int(l[0]))
    v.append(float(l[1]))
    myline = velFile.readline()
velFile.close()

massAns = newtonDividedDifference(time_mass[4:9], m[4:9], 4, 25)
velAns = newtonDividedDifference(time_vel[4:9], v[4:9], 4, 25)

prevMass = newtonDividedDifference(time_mass[5:9], m[5:9], 3, 25)
prevVel = newtonDividedDifference(time_vel[5:9], v[5:9], 3, 25)

print('Mass(in metric ton unit) at t=25s:', massAns)
print('Velocity(in m/sec unit) at t=25s:', velAns)

relMass = abs(massAns - prevMass)/massAns
relVel = abs(velAns - prevVel)/velAns

print('Relative mass error:', relMass*100)
print('Relative velocity error:', relVel*100)

plt.subplot(1, 2, 1)
plt.scatter(time_mass, m, c='blue')
plt.plot(25, massAns, 'ro')
plt.title('Mass')
plt.xlabel('time')
plt.ylabel('mass')
  
plt.subplot(1, 2, 2)
plt.scatter(time_vel, v, c = 'green')
plt.plot(25, velAns, 'ro')
plt.title('Velocity')
plt.xlabel('time')
plt.ylabel('velocity')
  
plt.show()

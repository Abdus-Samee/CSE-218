import math

def func_val(x):
    return (2000*math.log(140000/(140000-2100*x)))-9.8*x

def trapezoidIntegration(n, a, b):
    h = (b-a)/n
    first = func_val(a)
    second = func_val(b)
    
    s = 0
    for i in range(1, n):
        s += func_val(a+i*h)
    
    ans = ((b-a) * (first + second + 2*s))/(2*n)
    
    return ans
        
def simpsonIntegration(n, a, b):
    s1 = 0
    s2 = 0
    t = []
    t.append(func_val(a))
    h = (b-a)/n
    i = a
    
    for _ in range(1, n):
        t.append(func_val(i+h))
        i += h    
    t.append(func_val(b))
    
    for i in range(1, n):
        if i%2 == 0:
            s2 += t[i]
        else:
            s1 += t[i]
            
    ans = ((b-a)*(t[0] + t[n] + 4*s1 + 2*s2))/(3*n)
    
    return ans
        
n = int(input('Enter number of sub-intervals:'))
print()

print('Trapezoidal Integration:')
print('Distance traversed by the rocket:', trapezoidIntegration(n, 8, 30))
print('{:<10} {:<10} {:^12}'.format('Segment', 'Value', 'Absolute Relative Error'))
prevAns = -1
for i in range(1, 6):
    ans = trapezoidIntegration(i, 8, 30)
    if i != 1:
       error = abs((ans-prevAns)/ans)*100 
       print("{:<10} {:<10.4f} {:^10.4f}".format(i, ans, error))
    else:
       print("{:<10} {:<10.4f} {:^10}".format(i, ans, "--"))
    prevAns = ans

print()
print('Simpson\'s 1/3 Integration:')
print('Distance traversed by the rocket:', simpsonIntegration(2*n, 8, 30))
print('{:<10} {:<10} {:^12}'.format('Segment', 'Value', 'Absolute Relative Error'))
prevAns = -1
for i in range(2, 11, 2):
    ans = simpsonIntegration(i, 8, 30)
    if prevAns != -1:
        error = abs((ans-prevAns)/ans)*100 
        print("{:<10} {:<10.4f} {:^10.4f}".format(i, ans, error))
    else:
        print("{:<10} {:<10.4f} {:^10}".format(i, ans, "--"))
        prevAns = ans            

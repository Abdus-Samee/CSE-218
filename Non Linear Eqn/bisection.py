"""
Equation:
    x^3 - 2400x^2 - 3x + 2 = 0
x = [0, ]
"""

def bisection(lb, ub, e, iter):
    lv = lb**3-2400*(lb**2)-3*lb+2
    uv = ub**3-2400*(ub**2)-3*ub+2
    
    if lv*uv > 0:
        print("No root found")
        return
    
    prev_mid = (lb+ub)/2
    f_lb = lb**3-2400*(lb**2)-3*lb+2
    f_mid = prev_mid**3-2400*(prev_mid**2)-3*prev_mid+2
    
    if f_lb*f_mid < 0 :
        ub = prev_mid
    elif f_lb*f_mid > 0:
        lb = prev_mid
    else:
        return prev_mid
    
    for _ in range(iter):
        mid = (lb+ub)/2
        f_lb = lb**3-2400*(lb**2)-3*lb+2
        f_mid = mid**3-2400*(mid**2)-3*mid+2
        
        if f_lb*f_mid < 0 :
            ub = mid
        elif f_lb*f_mid > 0:
            lb = mid
        else:
            return mid
        
        rel_error = abs(mid - prev_mid)/mid
        if rel_error <= e:
            return mid
        else:
            prev_mid = mid
            

#calling bisection method
ans = bisection(0, 1, 0.005, 20)
if ans is not None:
    print("Molar dissociation: " + str(ans))

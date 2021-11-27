def bisection(lb, ub, e, iter):
    lv = lb**3-2400*(lb**2)-3*lb+2
    uv = ub**3-2400*(ub**2)-3*ub+2
    
    if lv*uv > 0:
        print("No root found")
        return
    
    d = {}
    prev_mid = (lb+ub)/2
    f_lb = lb**3-2400*(lb**2)-3*lb+2
    f_mid = prev_mid**3-2400*(prev_mid**2)-3*prev_mid+2
    
    if f_lb*f_mid < 0 :
        ub = prev_mid
    elif f_lb*f_mid > 0:
        lb = prev_mid
    else:
        d[0] = (prev_mid, 0)
    
    for i in range(iter):
        mid = (lb+ub)/2
        f_lb = lb**3-2400*(lb**2)-3*lb+2
        f_mid = mid**3-2400*(mid**2)-3*mid+2
        
        if f_lb*f_mid < 0 :
            ub = mid
        elif f_lb*f_mid > 0:
            lb = mid
        else:
            return d
        
        rel_error = abs(mid - prev_mid)/mid
        
        #printing table data
        d[i+1] = (mid, rel_error)
        
        if rel_error <= e:
            return d
        else:
            prev_mid = mid
            

d = bisection(0, 1, 0.005, 20)
if d is not None:
    print("{:<8} {:<17} {:<17}".format('Iteration', 'Root', 'Relative error'))
    for k, v in d.items():
        print("{:^8} {:^17.10f} {:^17.10f}".format(k, v[0], v[1]))
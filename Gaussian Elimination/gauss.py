import numpy as np

def GaussianElimination(A, B, d=True):
    #forward elimination in (n-1) steps
    '''
      Step like switching rows when pivot becomes
      0 has been ignored and a simple implementation
      has been done :)
    '''
    col = 0
    for i in range(len(A[0])-1):
        for j in range(i, len(A[0])-1):
            div = A[j+1][col]/A[i][col]
            temp = []
            for idx in range(len(A[j+1])):
                temp.append(A[j+1][idx]-A[i][idx]*div)
            A[j+1] = temp
            B[j+1][0] -= (B[i][0]*div)
            
            if d:
                print('\n---------------')
                print('Matrix A: ')
                print(np.matrix(A))
                print('\nMatrix B: ')
                print(np.matrix(B))
                print('---------------\n')
        col += 1
        
    ans = []
    loop = len(A[0])-1
    while loop >= 0:
        val = 0
        for i in range(loop+1, len(A[0])):
            val += (A[loop][i]*ans[len(A[0])-1-i])
        ans.append((B[loop][0] - val)/A[loop][loop])
        loop -= 1
        
    ans.reverse()
    col_mat = np.matrix(ans)
    col_mat = col_mat.T
    
    return col_mat

var = int(input())

A = []
B = []

for i in range(var):
    val = input().split(' ')
    A.append([float(i) for i in val])
    
for i in range(var):
    val = float(input())
    B.append([val])
    
ans = GaussianElimination(A, B)
print('\nThe required answer is: ')
for i in range(var):
    print("%.4f"%ans[i][0])

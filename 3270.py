import math

numC = {}

def catalan(n):
    
    if n in numC:
        return numC[n]
        
    if n<=1:
        numC[n]=1
        return 1
        
    res = math.comb(2*n,n)//(n+1)
    
    numC[n] = res
    return res

num = (int(input()))
print(catalan(num+1))

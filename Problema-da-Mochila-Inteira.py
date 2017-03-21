import numpy as np

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    i = n
    j = W
    k = 0
    prod=[]
    index=[]
    while K[i][j] >0:
        if K[i-1][j] != K[i][j]:
            prod.append(wt[val.index(val[i-1])])
            index.append(val.index(val[i-1])+1)
            j = j - wt[i-1] 
        i = i-1
        
    index.sort()        
    prod.sort()
    
    return index, prod, K[n][W]


n,W = [int(i) for i in input().split()]
wt  = [int(i) for i in input().split()]
val = [int(i) for i in input().split()]


index, prod, valor = knapSack(W, wt, val, n)
print("valor: %d"%(valor))
print("posições escolhidas: ", end='')
[print(i, end=' ') for i in index]
print()
print("produtos escolhidos: ", end='')
[print(i, end=' ') for i in prod]
print()

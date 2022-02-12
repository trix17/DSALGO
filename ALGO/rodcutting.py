"""import sys

def cutrod(price, n):
    if n == 0:
        return 0


    maximum = -sys.maxsize
    for i in range(1,n+1):
        maximum = max(maximum, price[i-1]+cutrod(price, n-i))
    return maximum"""
import sys
def cutrod(price, n):
    r = [0]*n
    r[0] = 0

    for j in range(1,n+1):
        q = -sys.maxsize
        for i in range(1, j+1):
            q = max(q,price[i-1]+ r[j-i])
        r[j] = q
    return r[n]
price = [1,5,8,9,10,17,20]
n = 4

print("the total profit is", cutrod(price, n))
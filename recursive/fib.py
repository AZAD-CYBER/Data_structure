def fib(n):
    if n<=1:
        return n
    else:
        a= fib(n-1)+fib(n-2)
    
        return a
print(fib(5))

from collections import defaultdict
m=defaultdict(int)
def tribonacci(n):
    if m[n]:
        return m[n]
    if n<=2:
        m[n]=n
        return m[n] 
    m[n]=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
    return m[n]
L=[]
for i in range(15):
    L.append(tribonacci(i))
print(" ".join(str(x) for x in L))
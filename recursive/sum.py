def Sum(n,sum1):
    if n==0:
        return sum1
    sum1+=n
    a= Sum(n-1,sum1)
    return a
print(Sum(5,0))

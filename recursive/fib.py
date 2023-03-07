def fib(n):
    if n<=1:
        return n
    else:
        return  fib(n-1)+fib(n-2)
        
print(fib(5))


# def printFactorial(a, b, n):
#     if n == 0:
#         return
#     print(a)
#     printFactorial(a=b, b=a+b, n=n-1)

# printFactorial(0, 1, 5)

# from collections import defaultdict
# m=defaultdict(int)
# def tribonacci(n):
#     if m[n]:
#         return m[n]
#     if n<=2:
#         m[n]=n
#         return m[n] 
#     m[n]=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
#     return m[n]
# L=[]
# for i in range(15):
#     L.append(tribonacci(i))
# print(" ".join(str(x) for x in L))
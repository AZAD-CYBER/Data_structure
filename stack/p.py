# li=[]
# i=0
# j=0
# z=0
# for i in range(2):
#     if i+j+z!=3:
#             li.append([i,j,z])
# for j in range(2):
#     if i+j+z!=3:
#             li.append([i,j,z])
# for z in range(3):
#     if i+j+z!=3:
#             li.append([i,j,z])
# print(li)

# print(    [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n ]
#     )

# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
    

#     winner=max(arr)
#     r=[]
#     for i in arr:
#         if i <winner:
#             r.append(i)
#     print(max(r))


# le=int(input())
# for i in range(le):
#     name = input()
#     score = float(input())
#     le.append([name,score])
# s=[]
# k=[]
# for i in le:
#     s.append(i[1])
# s.sort()
# for j in le:
#     if s[1]==j[1]:
#         k.append(j)
# k.sort()
# for i in k:
#     print(*i[0],sep="")

# from collections import defaultdict
# d=defaultdict(list)

# a,b=list(map(int,input().split()))

# for i in range(1,a+1):
#     n=input()
#     d[n].append(str(i))



# for j in range(1,b+1):
#     n1=input()
#     print(" ".join(d[n1]) or -1)

# print(None or "dieijis")

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            print(c)
            a = b
            b = c
        
 
# Driver Program
 
fibonacci(9)
from collections import deque
import copy
def funGame (arr):
    a = deque(arr)
    b = copy.deepcopy(a)
    print(b)
    c= []
    while(len(a)!=0 and len(b)!=0):
        i = 0
        j = 1
        if a[i]>b[-j]:
            c.append(1)
            b.pop()
        elif a[i]<b[-j]:
            c.append(2)
            a.popleft()
        elif a[i]==b[-j]:
            c.append(0)
            b.pop()
            a.popleft()
        if len(a)==0:
            break
    return c
n = int(input())
arr = map(int, input().split())
out_ = funGame(arr)
print (' '.join(map(str, out_)))
#Question 2
def findGoodPairs( a, n, k):
    #dic banaya
    di={}
    for i in range(n):
        nu=a[i]
        if nu not in di:
            di[nu]=[]
        di[nu].append(i) # index ko append kar raha 
    print(di)
    print(di.values())

    res=0
    for val in di.values():
        print(val)
        for i in range(len(val)):
            l,h=i,len(val) # low aur high kar raha
            
            while l+1<h:
                mid=(h+l)//2
                print(mid,"mid")
                if val[mid]-val[i]>=k:
                    h=mid
                    print(h,"high")
                else:
                    l=mid
                    print(l,"low")
            res+=len(val)-h
    
    return res
n = 5
k = 2
a = [1, 2, 2, 1, 2]
print(findGoodPairs( a, n, k))
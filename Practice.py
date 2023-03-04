def minimumScore(s,t):
    ns,nt=len(s),len(t)
    best=nt
    left=[ns for _ in range(nt)]
    
    j=0 #pointer fot t 
    for i in  range(ns):
        if s[i]==t[j]:
            left[j]=i
            # print(left)
            best=min(best,nt-j-1)
            j+=1
        if j==nt:
            return 0

    right=[-1 for _ in range(nt)]
    j=nt-1
    for i in range(ns-1,-1,-1):
        if s[i]==t[j]:
            right[j]=i
            best=min(best,j)
            j-=1
            
    i=-1
    for j in range(nt):
        while i+1<j and left[i+1]<right[j]:
            i+=1
        if i!=-1:
            best=min(best,j-i-1)

    return best
print(minimumScore("abacaba", "bzaa"))
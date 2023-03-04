
def lastOccour(arr,size,i,target,pos):
    if i==size:
        return pos
    if arr[i]==target:
        pos=i
    
    return lastOccour(arr,size,i+1,target,pos)


arr=[1,2,3,2,3,4,3,4,6,5,3]
size=len(arr)
i=0
target=4
pos=-1
print(lastOccour(arr,size,i,target,pos))
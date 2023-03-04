res=[]
def firstOccour(arr,size,i,target):
    if len(res)<1:
        return -1
    if i==size:
        return res[0]
   
    if arr[i]==target:
        res.append(i)
   
    return firstOccour(arr,size,i+1,target)
   

arr=[1,2,3,2,3,4,3,6,5,3]
size=len(arr)
i=0
target=4
print(firstOccour(arr,size,i,target))
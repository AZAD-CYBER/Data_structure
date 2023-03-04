# Time Complexity	O(n)
# Best Case	O(1)
# Worst Case	O(n)
# Space Complexity	O(1)
# Avg. Comparisons	(n+1)/2

def linear(a,key):
    for i in range(len(a)):
        if a[i]==key:
            return i
        return -1

a = [10, 23, 40, 1, 2, 0, 14, 14, 50, 9]
key = 142
flag = 0
result=linear(a,key)
if result==-1:
    print("The item {} was not found".format(key))
else:
     print("The item {} was  found {} index".format(key,result))
# for i in range(len(a)):
#     if a[i] == key:
#         flag = 1
#         found = a.index(a[i])

# if flag == 0:
#     print("Item not found ")
# else:
#     print("Item found at ", found + 1)

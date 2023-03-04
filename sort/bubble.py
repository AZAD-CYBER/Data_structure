#Performance Based Analysis of Bubble Sort Algorithm
# Pros
# Easy to implement
# Cool to implement
# Gives the largest value of array in the first iteration itself.
# Or the smallest value of array in the first iteration itself (Minor tweak in implementation)
# No demand for large amounts of memory for operation
# Cons
# Noob (Bad) algorithm 😀
# Very horrible time complexity of O(n2)
# Interesting Facts
# Average and worst case time complexity: o(n2)
# Best case time complexity: n when array is already sorted.
# Worst case: when the array is reverse sorted.


arr = [5, 3, 1, 9, 8, 2, 4, 7]

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

def bubble(arr,n):
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
arr = [5, 3, 1, 9, 8, 2, 4, 7]
print(bubble(arr,len(arr)))










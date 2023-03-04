# Binary Search in python
"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <=high:

        mid = (high+low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return low


array = [3, 4, 5, 6, 7, 8, 9]
x = 50

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
# Time Complexity (Best)	Ω(1)
# Time Complexity (Avg)	Θ(log n)
# Time Complexity (Worst)	O(log n)
# Space Complexity	O(1)


# def binary(arr, start, last, key):
#     if last >= start:
#         mid = (start + last) // 2
#         if arr[mid] == key:
#             return mid + 1
#         elif arr[mid] < key:
#             return binary(arr, mid + 1, last, key)
#         else:
#             return binary(arr, start, mid - 1, key)
#     return -1

 
# It returns location of x in given array arr
# if present, else returns -1
 
 
def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 
 
# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")


def main():
    a = [9, 26, 33, 47, 53, 60, 75, 80, 86, 99]

    key = int(input("Enter the key "))

    location = -1

    location = binary(a, 0, len(a) - 1, key)

    if location != -1:
        print("Item found ", location)
    else:
        print("Item not found ")


if __name__ == "__main__":
    main()



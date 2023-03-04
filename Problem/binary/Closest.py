def closest_element(array, target):
    array.sort()
    left, right = 0, len(array) - 1
    closest = float("inf")
    closest_element = None
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return array[mid]
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        print(array[mid])
        if abs(array[mid] - target) < closest:
            closest = abs(array[mid] - target)
            closest_element = array[mid]
    return closest_element

array = [1, 2, 3, 4, 46, 9, 56]
target = 11
print(closest_element(array, target))

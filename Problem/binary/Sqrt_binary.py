"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        print(mid,left,right)
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            print(left,"l")
        else:
            right = mid - 1
            print(right,"re")
    return right
print(mySqrt(8))
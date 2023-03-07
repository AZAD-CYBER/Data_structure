def power(x,n):
    if n!=0:
        return x*power(x,n-1)
    else:
        return 1
print(power(9,2))

# Third Recursion's Return:
# 1

# This returned 1 will then be multiplied by the "x" passed in the previous call i.e power(9,1).

# Second Recursion's Return:
# 9 * 1 = 9

# Similarly, this returned 9 will again be multiplied by the "x" passed in its previous call i.e power(9,2).

# First Recursion's Return:
# 9 * 9 = 81

# Thus the Final answer for power(9,2) is 81.


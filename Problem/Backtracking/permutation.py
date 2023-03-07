
# def permutations(nums):
#     result=[]

#     #base case
#     if len(nums)==1:
#         return [nums[:]]

#     for i in range(len(nums)):
#         n=nums.pop(0)
#         perms=permutations(nums)
#         print(perms,n)
#         for perm in perms:
#             perm.append(n)
            
#         result.extend(perms)
        
#         nums.append(n)
#         print("nums",nums)
#     return result


def permutations(nums):

    result = [[]]
    for n in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_result.append(perm[:i] + [n] + perm[i:])
                print(perm[:i],[n] , perm[i:])
        result = new_result
    return result

print(permutations([1,2,3]))



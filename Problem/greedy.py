# def coinChange(coins, amount):
#     coins.sort(reverse=True)
#     res = 0
#     i = 0

#     while amount > 0 and i < len(coins):
#         if coins[i] <= amount:
#             num = amount // coins[i]
#             res += num
#             amount -= num * coins[i]
#         i += 1

#     if amount == 0:
#         return res
#     else:
#         return -1

# print(coinChange([2], 3))
# Output: -1

# print(coinChange([186, 419, 83, 408], 6249))
# Output: 20

def coinChange(coins, amount):
    # Create dp array with all elements initialised to infinity
    dp = [float('inf')] * (amount + 1)
    
    # For 0 amount, 0 coins are required
    dp[0] = 0
    
    # Iterate over all amounts from 1 to amount
    for i in range(1, amount + 1):
        # Try using each coin from coin
        for coin in coins:
            # Check if that coin lends to a smaller coins requirement as compared to the previously calculated one.
            if i - coin >=0:
                print("WORK",dp[i],dp[i-coin])
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # If it is not possible to make the amount, return -1 else return dp[amount]
   
    return dp[amount] if dp[amount] != float('inf') else -1
print(coinChange([1, 2, 5], 11)) # Output: 3
# print(coinChange([2], 3)) # Output: -1
# print(coinChange([186, 419, 83, 408], 6249)) # Output: 20

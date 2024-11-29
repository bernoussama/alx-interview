#!/usr/bin/python3
""" 
Making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize a large value for comparison (total + 1 is sufficient)
    dp = [float("inf")] * (total + 1)
    # Base case: no coins are needed for a total of 0
    dp[0] = 0

    # Populate the DP table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, total cannot be reached
    return dp[total] if dp[total] != float("inf") else -1

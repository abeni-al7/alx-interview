#!/usr/bin/python3
"""Coin change problem"""


def makeChange(coins, total):
    """Solution for Coin Change problem"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        if dp[total] != float('inf'):
            return dp[total]
    return -1 if dp[total] == float('inf') else dp[total]

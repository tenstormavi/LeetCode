"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 10^4
"""

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ## Bottom-Up: Tabulation
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            # build the amount with all possible given coins
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        # return only if it doesn't store the default value
        return dp[amount] if dp[amount] != float('inf') else -1

        ## Top-Down
        ## Approach: At each stage, 3 choices are available. Use all the choices one
        ## by one and return the minimum one.

        def solveRec(amount, dp):
            # Base case
            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if dp[amount]:
                return dp[amount]

            res = float('inf')
            for coin in coins:
                ans = solveRec(amount - coin, dp)
                if ans != float('inf'):
                    res = min(res, 1 + ans)  # 1 plus because of current coin
            dp[amount] = res
            return dp[amount]

        dp = collections.defaultdict(int)
        res = solveRec(amount, dp)
        return res if res != float('inf') else -1

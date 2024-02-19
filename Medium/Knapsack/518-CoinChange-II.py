"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any
combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Approach: Can't use the approach of Coin Change (LC 322) as 2,2,1 and 2,1,2 is counted as 1.
        # No duplicates is allowed in the question.

        ## Recursion + Memoization
        def solve(idx, amount, dp):
            # Base case
            if amount == 0:
                return 1

            if amount < 0 or idx < 0:
                return 0

            if (idx, amount) in dp:
                return dp[(idx, amount)]

            # We have to choose both the values:
            # Not considering the curr value + Considering the curr value
            dp[(idx, amount)] = solve(idx - 1, amount, dp) + solve(idx, amount - coins[idx], dp)
            return dp[(idx, amount)]

        dp = defaultdict(int)
        n = len(coins)
        return solve(n - 1, amount, dp)

        ## Recursion
        def solve(idx, amount):
            # Base case
            if amount == 0:
                return 1

            if amount < 0 or idx < 0:
                return 0

            # We have to choose both the values:
            # 1) Considering the curr value
            # 2) Not considering the curr value
            res = solve(idx - 1, amount) + solve(idx, amount - coins[idx])

            return res

        n = len(coins)
        return solve(n - 1, amount)

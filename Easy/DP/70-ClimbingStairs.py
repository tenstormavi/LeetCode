"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

import collections


class Solution:
    memo = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        # Approach: Tabulation (Bottom-Up)
        self.memo[1] = 1
        self.memo[2] = 2
        for i in range(3, n + 1):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2]
        return self.memo[n]

        # Approach: Memoization (Top-Down)
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]

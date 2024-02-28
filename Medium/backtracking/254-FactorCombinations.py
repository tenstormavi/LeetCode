"""
Numbers can be regarded as the product of their factors.
    For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

Example 1:
Input: n = 1
Output: []

Example 2:
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]

Example 3:
Input: n = 37
Output: []

Constraints:
    1 <= n <= 107
"""


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # Approach: Similar to combination sum
        # At every point we decide if to take something or not take it. if we decide
        # to ditch a value at an index, we are never allowed to take it again if we go
        # down that respective path.

        # Calculate the factors first
        factors = []
        # given start from 2
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                factors.append(i)

        # Solve using backtrack
        def backtrack(idx, balance, path):
            # Base case
            # 1. idx == len(factors)
            # 2. n == 1

            if idx == len(factors):
                return

            if balance == 1:
                if len(path) > 1:
                    # result.append(path.copy())
                    result.append(path[:])
                    return

            for i in range(idx, len(factors)):
                value = factors[i]
                if balance % value == 0:
                    backtrack(i, balance // value, path + [value])

        result = []
        backtrack(0, n, [])
        return result

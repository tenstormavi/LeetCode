"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
    -231 <= n <= 231 - 1
"""

# Approach 1: Keep dividing the number by 4 unless you hit an odd number.
# Complexity - O(log(N))

# Approach 2:
# x = 4^a -> a = log4(x) = 1/2 log2(x)
# Hence let's simply check if log2(x) is an even number.
# Complexity - O((1))

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Solution 1
        if n == 0:
            return False

        while n % 4 == 0:
            n /= 4
        return n == 1

        # Solution 2:
        return n > 0 and math.log2(n) % 2 == 0

"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
    -231 <= n <= 231 - 1
"""

# Approach 1: Keep dividing the number by 2 unless you hit an odd number.
# Complexity - O(log(N))

# Approach 2: Log Operation - if a number is power of 2. Then Log2(N) will be an integer number so
# ceil and floor value will be same.
# And modulus of an integer with 1 will always be 0 so that can be another answer.

import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        # Solution 1
        # cal = math.log2(n)
        # return True if math.ceil(cal)==math.floor(cal) else False

        # Solution 2
        return math.log2(n) % 1 == 0

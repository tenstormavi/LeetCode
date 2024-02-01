"""
Given string num representing a non-negative integer num, and an integer k, return the smallest
possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
"""

import sys
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Approach: stack should be monotonic increasing
        # Remove the most significant digit before least and remove only k times
        sys.set_int_max_str_digits(0)
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            stack.append(char)

        # Might total number of K integers is not get deleted yet. eg 12345
        # Then remove the last K digits from last
        stack = stack[:len(stack) - k]
        res = "".join(stack)

        # what if res is an empty string
        return str(int(res)) if res else "0"

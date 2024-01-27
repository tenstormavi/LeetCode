"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Solution 1:
        oddChars = set()

        for c in s:
            if c in oddChars:
                oddChars.remove(c)
            else:
                oddChars.add(c)

        return len(oddChars) <= 1

        # Solution 2:
        return sum(v % 2 for v in Counter(s).values()) <= 1

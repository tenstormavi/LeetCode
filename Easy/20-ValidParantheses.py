"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        d[")"] = "("
        d["]"] = "["
        d["}"] = "{"

        stack = []
        count = 0

        for i in range(len(s)):
            if s[i] not in d.keys():
                stack.append(s[i])
            # len(stack) will be 0 in cases like only "]"
            elif len(stack) == 0 or d[s[i]] != stack.pop():
                return False
        return len(stack) == 0

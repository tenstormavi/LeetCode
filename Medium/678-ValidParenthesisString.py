"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Approach: we need to balance all the opening and closing backets.
        # First we will balance all the closing bracket with count of opening backet.
        # If that is sufficient then okay otherwise we will use the count of start for balancing.
        # Then if there will be any opening bracket needs to be balanced, we will balance that
        # using star count.

        open_stack = []  # saving index
        star_stack = []  # saving index
        # Balance the closing bracket
        for i in range(len(s)):
            if s[i] == "(":
                open_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                # Balance the closing bracket with open bracket count
                if len(open_stack) > 0:
                    open_stack.pop()
                elif len(star_stack) > 0:
                    # Balance the closing bracket with star bracket count
                    star_stack.pop()
                else:
                    # Can't balance since both open and start counts are not exhausted
                    return False

        # Balance the remaining open bracket with star count
        if len(star_stack) < len(open_stack):
            # less star, more opening bracket
            return False

        for i in range(len(open_stack)):
            # open_stack - [3], star_stack - [0,1,2]
            if len(star_stack) > 0 and open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
        return True

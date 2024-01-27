"""
Given two strings s and t, return true if they are equal when both are typed into empty
text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Solution -> with constant space
        # Approach: we know character before # has to be deleted, so try to iterate in reverse
        # and compare each character one by one
        def nextValidChar(str, index):
            backspace = 0
            while index >= 0:
                if str[index] != "#" and backspace == 0:
                    # Ready to compare character
                    break
                elif str[index] == "#":
                    # Now backspace count charaters needed to skip
                    backspace += 1
                else:
                    # Skipping the count characters
                    backspace -= 1
                index -= 1
            return index

        index_s, index_t = len(s) - 1, len(t) - 1
        while index_s >= 0 or index_t >= 0:
            index_s = nextValidChar(s, index_s)
            index_t = nextValidChar(t, index_t)
            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""
            if char_s != char_t:
                return False
            index_s -= 1
            index_t -= 1
        return True


        # Solution -> with extra space
        def makeString(stack, s):
            for i in s:
                if i != "#":
                    stack.append(i)
                elif len(stack) > 0:
                    stack.pop()
            return "".join(stack)

        res_s = makeString([], s)
        res_t = makeString([], t)
        return res_s == res_t


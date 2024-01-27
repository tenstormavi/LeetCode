"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid
parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "((()()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to
split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:
    1 <= s.length <= 10^5
    s[i] is either '(' or ')'.
    s is a valid parentheses string.
"""

from collections import deque

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Solution:
        res = ""
        count = 0
        flag = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            else:
                count -= 1

            if count == 0:
                res += s[flag+1: i]
                flag = i + 1
        return res

        # Solution -> space not constant
        q = deque()
        openN = 0
        closedN = 0
        res = ""
        for i in s:
            if i == "(":
                openN += 1
            else:
                closedN += 1
            q.append(i)

            if openN == closedN:
                q.popleft()
                q.pop()
                res += ("".join(q))
                q.clear()
        return res

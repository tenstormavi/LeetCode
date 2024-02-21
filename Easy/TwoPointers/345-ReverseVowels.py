"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
    1 <= s.length <= 3 * 10^5
    s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        v = 'aeiouAEIOU'
        while left < right:
            if s[left] in v and s[right] in v:
                s[left], s[right] = s[right], s[left]
                left += 1; right -= 1
            elif s[left] not in v:
                left += 1
            elif s[right] not in v:
                right -= 1
        return ''.join(s)

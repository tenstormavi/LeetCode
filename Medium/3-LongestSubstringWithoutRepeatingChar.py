"""
Given a string s, find the length of the longest
substring
without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        hash_map = {}
        while r < len(s):
            if s[r] in hash_map:
                hash_map[s[r]] += 1
            else:
                hash_map[s[r]] = 1
            while hash_map[s[r]] > 1:
                hash_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

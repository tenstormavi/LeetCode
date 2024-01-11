"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the
window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = dict()
        for c in t:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        start, end = 0, 0
        num_of_chars_to_be_included = len(t)
        min_window_start = 0
        min_window_length = len(s) + 1
        while end < len(s):
            if s[end] in hash_map:
                if hash_map[s[end]] > 0:
                    num_of_chars_to_be_included -= 1
                hash_map[s[end]] -= 1
            while num_of_chars_to_be_included == 0:
                if (end - start) + 1 < min_window_length:
                    min_window_length = (end - start) + 1
                    min_window_start = start
                if s[start] in hash_map:
                    hash_map[s[start]] += 1
                    if hash_map[s[start]] > 0:
                        num_of_chars_to_be_included += 1
                start += 1
            end += 1
        if min_window_length == len(s) + 1:
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]

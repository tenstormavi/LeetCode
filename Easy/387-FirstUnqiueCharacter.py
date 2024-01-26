"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
"""

from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Solution - Ordered Dict
        d = OrderedDict()  # char_count, idx
        seen = set()
        for idx, char in enumerate(s):
            if char not in seen:
                seen.add(char)
                d[char] = idx
            else:
                if char in d:
                    del d[char]

        for key, value in d.items():
            return value
        return -1

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach: use hash map
        count = defaultdict(int)

        # count the frequency of characters in sting s
        for i in s:
            count[i] += 1

        # count the frequency of characters in sting t
        for i in t:
            count[i] -= 1

        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        return True

        # Approach: Sort and check
        return sorted(s) == sorted(t)

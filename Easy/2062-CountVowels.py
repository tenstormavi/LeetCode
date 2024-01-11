"""
A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of
vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

Example 1:
Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:
Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:
Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

Constraints:
    1 <= word.length <= 100
    word consists of lowercase English letters only.
"""

from collections import defaultdict
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        return sum ( set(word[i:j])==set("aeiou") for i in range(0,len(word)-4) for j in range(i+5,len(word)+1) )

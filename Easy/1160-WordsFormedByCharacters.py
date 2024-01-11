"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    words[i] and chars consist of lowercase English letters.
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def cal_character(word):
            char_map = {}
            for i in word:
                if i not in char_map:
                    char_map[i] = 1
                else:
                    char_map[i] += 1
            return char_map

        ans = 0
        for word in words:
            flag = 0
            char_counts = cal_character(word)
            for i in char_counts:
                if char_counts[i] <= chars.count(i):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                ans += len(word)
        return ans

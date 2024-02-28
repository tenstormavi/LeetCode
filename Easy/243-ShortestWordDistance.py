"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
return the shortest distance between these two words in the list.

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Constraints:
    2 <= wordsDict.length <= 3 * 10^4
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
    word1 != word2
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        wrd1, wrd2 = -1, -1
        dist = float('inf')
        for idx, word in enumerate(wordsDict):
            if word == word1:
                wrd1 = idx
            elif word == word2:
                wrd2 = idx

            if wrd1 != -1 and wrd2 != -1:
                dist  = min(dist, abs(wrd2 - wrd1))

        return dist

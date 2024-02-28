"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without
changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
    1 <= s.length <= 1000
    s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Approach: use longest common subsequence approach LC 1143
        # Get all subsequence from s and reverse s. The longest common
        # subsequence will be our answer. Palindrome is string which is same
        # string even if we reverse it.

        # Tabulation -> Bottom up - TC O(n*m)
        def solveTab(text1, text2):
            # Initialise base on base case of recursion
            dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

            for i in range(len(text1)):
                for j in range(len(text2)):
                    if text1[i] == text2[j]:
                        dp[i + 1][j + 1] = 1 + dp[i][j]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            return dp[-1][-1]

        text1 = s
        text2 = s[::-1]
        return solveTab(text1, text2)

        # Recursion + Memoization -> Top Down - TC O(n*m)
        def solveMem(text1, text2, i, j, dp):
            # Base case
            if i == len(text1) or j == len(text2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            if text1[i] == text2[j]:
                dp[i][j] = 1 + solveMem(text1, text2, i + 1, j + 1, dp)
            else:
                dp[i][j] = max(solveMem(text1, text2, i + 1, j, dp), solveMem(text1, text2, i, j + 1, dp))
            return dp[i][j]

        text1 = s
        text2 = s[::-1]
        dp = [[-1] * (len(text2) + 1) for i in range(len(text1) + 1)]
        return solveMem(text1, text2, 0, 0, dp)

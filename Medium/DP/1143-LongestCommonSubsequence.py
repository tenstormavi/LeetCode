"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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

        dp = [[-1] * (len(text2) + 1) for i in range(len(text1) + 1)]
        return solveMem(text1, text2, 0, 0, dp)

        # Recursion - TC O(2^(n+m))
        def solveRec(text1, text2, i, j):
            # Base case
            if i == len(text1) or j == len(text2):
                return 0

            ans = 0
            if text1[i] == text2[j]:
                ans = 1 + solveRec(text1, text2, i + 1, j + 1)
            else:
                ans = max(solveRec(text1, text2, i + 1, j), solveRec(text1, text2, i, j + 1))
            return ans

        return solveRec(text1, text2, 0, 0)

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Approach: At every character we have 3 choices insert, delete and replace.
        # If the character is mactching, check the rest of the characters otherwise
        # check all the choices and return minimun among all three.

        def solveRec(word1, word2, i, j):
            # Base cases
            # If word1 length is smaller than word2 length
            if i == len(word1):
                return len(word2) - j

            # If word2 length is smaller than word1 length
            if j == len(word2):
                return len(word1) - i

            ans = 0
            if word1[i] == word2[j]:
                return solveRec(word1, word2, i + 1, j + 1)
            else:
                # Insert
                ins_ans = 1 + solveRec(word1, word2, i, j + 1)

                # Delete
                del_ans = 1 + solveRec(word1, word2, i + 1, j)

                # Replace
                rep_ans = 1 + solveRec(word1, word2, i + 1, j + 1)

                ans = min(ins_ans, del_ans, rep_ans)
            return ans

        # Top Down
        def solveMemo(word1, word2, i, j, dp):
            # Base cases
            # If word1 length is smaller than word2 length
            if i == len(word1):
                return len(word2) - j

            # If word2 length is smaller than word1 length
            if j == len(word2):
                return len(word1) - i

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            if word1[i] == word2[j]:
                return solveMemo(word1, word2, i + 1, j + 1, dp)
            else:
                # Insert
                ins_ans = 1 + solveMemo(word1, word2, i, j + 1, dp)

                # Delete
                del_ans = 1 + solveMemo(word1, word2, i + 1, j, dp)

                # Replace
                rep_ans = 1 + solveMemo(word1, word2, i + 1, j + 1, dp)

                dp[i][j] = min(ins_ans, del_ans, rep_ans)
            return dp[i][j]

        # Bottom Up
        def solveTab(word1, word2):
            dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

            # Made from base case of recursion
            for j in range(len(word2)):
                dp[len(word1)][j] = len(word2) - j

            # Made from base case of recursion
            for i in range(len(word1)):
                dp[i][len(word2)] = len(word1) - i

            for i in range(len(word1) - 1, -1, -1):
                for j in range(len(word2) - 1, -1, -1):
                    ans = 0
                    if word1[i] == word2[j]:
                        ans = dp[i + 1][j + 1]
                    else:
                        # Insert
                        ins_ans = 1 + dp[i][j + 1]

                        # Delete
                        del_ans = 1 + dp[i + 1][j]

                        # Replace
                        rep_ans = 1 + dp[i + 1][j + 1]

                        ans = min(ins_ans, del_ans, rep_ans)
                    dp[i][j] = ans
            return dp[0][0]

        # return solveRec(word1, word2, 0, 0) - TLE

        dp = [[-1 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        return solveMemo(word1, word2, 0, 0, dp)

        # return solveTab(word1, word2)

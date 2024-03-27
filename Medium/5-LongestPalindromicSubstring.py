"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach: Start expanding the palindrome from middle and check
        # both sides. There can be even length palindrome string and odd
        # length palindrome string. So check both.

        # TC - O(n^2)

        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1] # take r inclusive
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1] # take r inclusive
                l -= 1
                r += 1
        return res

        # Brute Force - Get all possible substrings and verify if it
        # is a palindrome or not. There are a total of n^2 such substrings
        # Since verifying each substring takes O(n) time, the run time
        # complexity is O(n^3).
        res = s[0] # case of "ac"
        res_len = 0
        if len(s) <= 1:
            return s
        for i in range(len(s)):
            for j in range(i + 1,len(s)):
                print(j - i + 1 > res_len)
                print(s[i:j + 1])
                if j - i + 1 > res_len and s[i:j + 1] == s[i:j + 1][::-1]:
                    res_len = j - i + 1
                    res = s[i:j + 1]
        return res

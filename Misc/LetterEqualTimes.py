"""
Write a function solution that given an integer N returns a string of length N containing as many different lower case
letters ('a'-'z') as possible, in which each letter occurs as an equal number of times.

Example 1:
Given N=3, the function may return "fig", "pea", "nut",etc. Each of these strings contains three different letters with
the same number of occurrences.

Example 2.
Given N=5, the function may return "mango","grape", "melon"

3.Given N=30,the function may
return "aabbcc...oo"(each letter from 'a' to 'o' occurs twice) the string contains 15 different letters.

write an efficient algorithm for the following assumptions: N is an integer within the range [1..200,000]
"""

from math import ceil


def solution(n):
    ans = ""
    occurrence = 1
    if n > 26:
        occurrence = ceil(n/26)
        n = n // 2
    for i in range(n):
        count = 1
        while count <= occurrence:
            ans += chr(ord('a') + i)
            count += 1
    return ans


# Test
print(solution(3))
print(solution(26))
print(solution(35))

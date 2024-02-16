"""
Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost associated with it.
Determine the maximum cost obtained by cutting the rod and selling its pieces.

Note:
1. The sizes will range from 1 to ‘N’ and will be integers.
2. The sum of the pieces cut should be equal to ‘N’.
3. Consider 1-based indexing.

Sample Input 1:
5
2 5 7 8 10
8
3 5 8 9 10 17 17 20

Sample Output 1:
12
24

Explanation of sample input 1:
Test case 1:
All possible partitions are:
1,1,1,1,1           max_cost=(2+2+2+2+2)=10
1,1,1,2             max_cost=(2+2+2+5)=11
1,1,3               max_cost=(2+2+7)=11
1,4                 max_cost=(2+8)=10
5                   max_cost=(10)=10
2,3                 max_cost=(5+7)=12
1,2,2               max _cost=(1+5+5)=12

Clearly, if we cut the rod into lengths 1,2,2, or 2,3, we get the maximum cost which is 12.

Test case 2:
Possible partitions are:
1,1,1,1,1,1,1,1         max_cost=(3+3+3+3+3+3+3+3)=24
1,1,1,1,1,1,2           max_cost=(3+3+3+3+3+3+5)=23
1,1,1,1,2,2             max_cost=(3+3+3+3+5+5)=22
and so on….

If we cut the rod into 8 pieces of length 1, for each piece 3 adds up to the cost. Hence for 8 pieces, we get 8*3 = 24.

Sample Input 2:
6
3 5 6 7 10 12

Sample Output 2:
18
"""


def cutRod(price, n):
    # Bottom-Up
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        ans = float('-inf')
        for j in range(i):
            cut = j + 1 # done as the index is 0 based
            cur_ans = price[j] + dp[i - cut]
            ans = max(ans, cur_ans)
        dp[i] = ans
    return dp[n]


    # Top-Down -> Recursion + Memoization
    def solve(price, n, dp):
        if n <= 0:
            return 0

        if dp[n] != 0:
            return dp[n]

        ans = float('-inf')
        for i in range(n):
            cut = i + 1 # done as the index is 0 based
            cur_ans = price[i] + solve(price, n - cut, dp)
            ans = max(ans, cur_ans)
        dp[n] = ans
        return dp[n]

    dp = [0] * (n + 1)
    return solve(price, n, dp)

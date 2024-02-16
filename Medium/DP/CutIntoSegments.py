"""
You are given an integer ‘N’ denoting the length of the rod. You need to determine the maximum number of segments
you can make of this rod provided that each segment should be of the length 'X', 'Y', or 'Z'.

Sample Input 1:
7 5 2 2
8 3 3 3

Sample Output 1:
2
0

Sample Input 2:
7 3 2 2
8 1 4 4

Sample Output 2:
3
8
"""


def cutSegments(n, x, y, z):
    # Write your code here.

    # Bottom-Up -> Tabulation
    def solveTab(n, x, y, z):
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if i - x >= 0 and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)

            if i - y >= 0 and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)

            if i - z >= 0 and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)

        if dp[n] < 0:
            return 0
        return dp[n]

    return solveTab(n, x, y, z)

    # Top-Down -> Recursion + Memoization
    def solve(n, x, y, z, dp):
        if n == 0:
            return 0

        if n < 0:
            return float('-inf')

        if dp[n] != -1:
            return dp[n]

        a = solve(n - x, x, y, z, dp) + 1
        b = solve(n - y, x, y, z, dp) + 1
        c = solve(n - z, x, y, z, dp) + 1

        dp[n] = max(a, b, c)
        return dp[n]

    dp = [-1] * (n + 1)
    res = solve(n, x, y, z, dp)
    if res < 0:
        return 0
    return res

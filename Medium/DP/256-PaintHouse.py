"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green.
The cost of painting each house with a certain color is different. You have to paint all the houses such that
no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
    For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting
    house 1 with color green, and so on...
Return the minimum cost to paint all houses.

Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Example 2:
Input: costs = [[7,6,2]]
Output: 2

Constraints:
    costs.length == n
    costs[i].length == 3
    1 <= n <= 100
    1 <= costs[i][j] <= 20
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Tabulation - Bottom up
        # costs[i][j] i is house, j is color

        # By observation, it only depends on previous row
        dp = [0, 0, 0]

        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]

        return min(dp)

        # Recursion - TLE
        def solveRec(i, prevColor):
            # Base case
            if i == len(costs):
                return 0

            res = float('inf')
            for color in range(3):
                if color != prevColor:
                    res = min(res, costs[i][color] + solveRec(i + 1, color))
            return res

        return solveRec(0, -1)

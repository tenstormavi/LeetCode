"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with
a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1
with color 2, and so on...
Return the minimum cost to paint all houses.

Example 1:
Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

Example 2:
Input: costs = [[1,3],[2,4]]
Output: 5

Constraints:
costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20

Follow up: Could you solve it in O(nk) runtime?
"""
from collections import defaultdict


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # Recursion + Memoization
        def solveMemo(idx, prevColor, dp):
            # Base case
            if idx == len(costs):
                return 0

            if (idx, prevColor) in dp:
                return dp[(idx, prevColor)]

            res = float('inf')
            for color in range(len(costs[0])):
                if color != prevColor:
                    res = min(res, costs[idx][color] + solveMemo(idx + 1, color, dp))
            dp[(idx, prevColor)] = res
            return res

        dp = defaultdict(int)
        return solveMemo(idx=0, prevColor=-1, dp=dp)

        # Recursion
        def solveRec(idx, prevColor):
            # Base case
            if idx == len(costs):
                return 0

            res = float('inf')
            for color in range(len(costs[0])):
                if color != prevColor:
                    res = min(res, costs[idx][color] + solveRec(idx + 1, color))
            return res

        return solveRec(idx=0, prevColor=-1)

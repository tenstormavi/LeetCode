"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach: Create a decision tree from 0 index and 1 index
        # with the cost to reach the top of the stairs. Then return
        # the minimum value between these.
        # https://www.youtube.com/watch?v=ktmzAZWkEZ0&ab_channel=NeetCode

        # Top-Down Approach
        cost.append(0) # The top stairs has zero cost

        for i in range(len(cost) - 3, -1, -1):
            # The last and second last price will be same only
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])


        # Bottom-Up Approach
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])

        # Bottom-Up Approach - constant space
        dp0 = cost[0]
        dp1 = cost[1]
        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur
        return min(dp0, dp1)

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        ###### Tabulation -> Bottom-Up with constant space; TC -> O(n)
        n = len(nums)
        prev2 = 0
        prev1 = nums[0]

        for i in range(1, n):
            incl = prev2 + nums[i]
            excl = prev1 + 0
            cur = max(incl, excl)
            prev2 = prev1
            prev1 = cur

        return prev1

        ###### Tabulation -> Bottom-Up; TC -> O(n), SC -> O(n)
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            incl = dp[i - 2] + nums[i]
            excl = dp[i - 1] + 0
            dp[i] = max(incl, excl)

        return dp[n - 1]

        ###### Recursive + Memoization -> Top-Down; TC -> O(n), SC -> O(n)
        def solv(nums, n, dp):
            # Base case
            if n < 0:
                return 0

            if n == 0:
                # Size of array is 1; max sum is that element only
                nums[0]

            if dp[n] != -1:
                return dp[n]

            # Recursive -> Top-Down
            incl = solv(nums, n - 2, dp) + nums[n]
            excl = solv(nums, n - 1, dp) + 0

            dp[n] = max(incl, excl)
            return dp[n]

        dp = [-1] * len(nums)
        res = solv(nums, len(nums) - 1, dp)
        return res

        ###### TLE #######
        ###### Recursive -> Top-Down
        def solv(nums, n):
            # Base case
            if n < 0:
                return 0

            if n == 0:
                # Size of array is 1; max sum is that element only
                nums[0]

            # Approach: There are two choices at every index either include the
            # current index or exclude the current index. If current index is included
            # its value will get added and index will jump 2 (i+2 or n-2) times as adjacent value is
            # not allowed to take. if Current index is not included its sum will not get added and
            # index will jump only 1 (i+1 or n-1) as taking adjacent value is possible now.
            incl = solv(nums, n - 2) + nums[n]
            excl = solv(nums, n - 1) + 0

            return max(incl, excl)

        res = solv(nums, len(nums) - 1)
        return res

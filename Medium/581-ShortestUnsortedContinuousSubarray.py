"""
Given an integer array nums, you need to find one continuous subarray such that if you only
sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0

Constraints:
    1 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5

Follow up: Can you solve it in O(n) time complexity?
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Approach: Iterate from start to end will give is the last index point
        # where the condition breaks of non-decresing. Similarly, iterating from
        # end to start will give the first index point.

        cur_max = float('-inf')
        cur_min = float('inf')
        idx_end = 0
        idx_start = 0

        for i in range(len(nums)):
            if nums[i] >= cur_max:
                cur_max = nums[i]
            else:
                idx_end = i

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= cur_min:
                cur_min = nums[i]
            else:
                idx_start = i

        # ans will be 1 in case of already sorted array
        ans = idx_end - idx_start + 1

        return ans if ans > 1 else 0

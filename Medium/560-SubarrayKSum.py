"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        d = dict()
        cur_sum = 0
        count = 0
        for i in nums:
            cur_sum += i
            if cur_sum == k:
                count += 1
            if cur_sum - k in d:
                count += d[cur_sum - k]
            if cur_sum in d:
                d[cur_sum] += 1
            else:
                d[cur_sum] = 1
        return count

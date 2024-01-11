"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Approach: Suppose 0 as -1 and 1 as 1
        cur_sum = max_len = 0
        d = {0: -1}
        for idx, num in enumerate(nums):
            if num == 1:
                cur_sum += 1
            else:
                cur_sum -= 1
            if cur_sum not in d:
                d[cur_sum] = idx
            else:
                max_len = max(max_len, idx - d[cur_sum])
        return max_len

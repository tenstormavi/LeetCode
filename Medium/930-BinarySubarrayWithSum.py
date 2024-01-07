"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
    1 <= nums.length <= 3 * 10^4
    nums[i] is either 0 or 1.
    0 <= goal <= nums.length
"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums, goal):
            start = end = cur_sum = count = 0
            while end < len(nums):
                cur_sum += nums[end]
                while cur_sum > goal and start <= end:
                    cur_sum -= nums[start]
                    start += 1
                count += (end - start + 1)
                end += 1
            return count

        # Approach: atmost(k) - atmost(k-1) gives exactly(k strictly)
        return atmost(nums, goal) - atmost(nums, goal - 1)

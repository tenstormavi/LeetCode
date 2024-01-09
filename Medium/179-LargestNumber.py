"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Approach: Selection sort + string comparision
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                first = str(nums[i]) + str(nums[j])
                second = str(nums[j]) + str(nums[i])
                if second > first:
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == 0:
            return "0"
        return "".join([str(x) for x in nums])

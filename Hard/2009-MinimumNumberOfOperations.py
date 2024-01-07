"""
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

    All elements in nums are unique.
    The difference between the maximum element and the minimum element in nums equals nums.length - 1.

For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

Example 1:
Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.

Example 2:
Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

Example 3:
Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Approach:
        # 1. Define the range using the minimum element in the array (Range = min_ele + size_of_array - 1).
        # This might get us wrong answe so we have to define at least all the elements as minimum element
        # once eg [2,6,7,8]
        # 2. Remove the duplicates from the array. eg [2,3,3,4]

        length = len(nums)
        nums = sorted(set(nums))
        res = length
        end = start = 0
        while start < length:
            # R = nums[start], nums[start] + len(nums) - 1
            while end < len(nums) and nums[end] < nums[start] + length:
                end += 1
            res = min(res, length - (end - start))
            start += 1
        return res

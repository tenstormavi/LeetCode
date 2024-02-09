"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum
is closest to target.

Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Approach: Maintain a diff which will tell us the closest sum
        # and at the same time save the sum to return as answer

        nums.sort()
        diff = float('inf')
        ans = 0
        for i in range(len(nums)):
            first_num = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                second_num = nums[j]
                third_num = nums[k]

                sum = first_num + second_num + third_num

                if sum == target:
                    return sum
                elif abs(target - sum) < diff:
                    diff = abs(target - sum)
                    ans = sum

                if sum > target:
                    k -= 1
                else:
                    j += 1
        return ans

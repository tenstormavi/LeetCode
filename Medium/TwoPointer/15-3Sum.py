"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 2:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values of the first number
            first_num = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                second_num = nums[j]
                third_num = nums[k]

                sum = first_num + second_num + third_num
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    triplets.add((first_num, second_num, third_num))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1  # Skip duplicate values of the second number
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1  # Skip duplicate values of the third number
        return triplets

        # Solution 1:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            first_num = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                second_num = nums[j]
                third_num = nums[k]

                sum = first_num + second_num + third_num
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    triplets.add((first_num, second_num, third_num))
                    j += 1
                    k -= 1
        return triplets

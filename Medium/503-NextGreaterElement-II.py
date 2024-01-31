"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in
the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:
    1 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Solution of circular list
        # Approach: for last element repeat the same array using i % n
        stack = []
        res = [-1] * len(nums)
        n = len(nums)

        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            if not stack:
                res[i % n] = -1
            else:
                res[i % n] = stack[-1]
            stack.append(nums[i % n])

        return res

        # Solution without circular list
        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]
            stack.append(nums[i])

        return res
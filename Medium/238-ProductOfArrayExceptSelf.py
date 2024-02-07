"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution: cummulative multiplication but constant space - Time -> O(n), Space -> O(1)
        # Approach: Calculate prefix multiplication and calculate posfix on the fly
        result = [1] * len(nums)

        # Calculate prefix multiplication
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Calulate the postfix multiplication in real time
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


        # Solution: By cummulative multiplication - Time and Space -> O(n)
        # Approach: Calculate cummulative left and right multiplication and multiply both at each index
        left_prod = [0] * len(nums)
        right_prod = [0] * len(nums)

        left_prod[0] = 1 # Left prefix multiplication of first number will be always 1
        right_prod[-1] = 1 # Right postfix multiplication of first number will be always 1

        # Fill prefix
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        # Fill prostfix
        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        result = []
        # Multiply left and right to get the final result
        for i in range(len(left_prod)):
            result.append(left_prod[i] * right_prod[i])
        return result


        # Solution: By Divison, Edge case when encounter 0
        # Approach: Count the occurance of zero so that it can be used while division
        product = 1
        zero_count = 0
        # Get the product of all the numbers except zeros
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num # Product of all the numbers

        # Prepare result based on zero_count and product of all numbers
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_count == 1:
                    # This is the only zero exists in the array
                    nums[i] = product
                else:
                    # More zeros are present so product will be 0
                    nums[i] = 0
            else:
                if zero_count > 0:
                    nums[i] = 0
                else:
                    nums[i] = product // nums[i]
        return nums

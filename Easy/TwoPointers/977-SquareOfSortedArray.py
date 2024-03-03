"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution
using a different approach?
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two Pointers Approach
        n = len(nums) - 1
        l = 0
        r = n
        ans = [0] * len(nums)

        while n >= 0:
            if abs(nums[l]) > abs(nums[r]):  # using n as index to fill so opposite logic
                ans[n] = abs(nums[l]) * abs(nums[l])
                l += 1
            else:
                ans[n] = abs(nums[r]) * abs(nums[r])
                r -= 1
            n -= 1
        return ans

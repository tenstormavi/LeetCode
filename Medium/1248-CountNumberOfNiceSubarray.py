"""
Given an array of integers nums and an integer k.
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        start = end = ans = odd_count = 0
        total_nice = 0
        while end < len(nums):
            if nums[end] % 2 == 1:
                odd_count += 1
                total_nice = 0
            while odd_count == k:
                if nums[start] % 2 == 1:
                    odd_count -= 1
                total_nice += 1
                start += 1
            ans += total_nice
            end += 1
        return ans

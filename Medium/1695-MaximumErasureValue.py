"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.
An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is,
if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = cur_sum = start = end = 0
        d = {}
        while end < len(nums):
            cur_sum += nums[end]
            print(cur_sum)
            d[nums[end]] = 1 + d.get(nums[end], 0)
            while d[nums[end]] > 1:
                cur_sum -= nums[start]
                d[nums[start]] -= 1
                start += 1
            ans = max(ans, cur_sum)
            end += 1
        return ans

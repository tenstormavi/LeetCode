"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

Constraints:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        for i in nums[:k]:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        max_sum = 0
        cur_sum = sum(nums[:k])

        if len(d) == k:
            max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            d[nums[i]] += 1
            d[nums[i - k]] -= 1

            if d[nums[i - k]] == 0:
                del d[nums[i - k]]

            if len(d) == k:
                max_sum = max(max_sum, cur_sum)

        return max_sum
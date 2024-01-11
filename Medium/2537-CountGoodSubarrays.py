"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example 2:
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i], k <= 10^9
"""

from collections import defaultdict


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pair = start = end = good = 0
        d = defaultdict(lambda: 0)
        while end < len(nums):
            d[nums[end]] += 1
            pair += d[nums[end]] - 1
            print(pair)
            while start <= end and pair >= k:
                # rest elements will also satisfy the case since pair == k is valid for them also
                good += len(nums) - end
                d[nums[start]] -= 1
                # pair need to remove = Frequency - 1
                pair -= d[nums[start]]
                if d[nums[start]] == 0:
                    del d[nums[start]]
                start += 1
            end += 1
        return good

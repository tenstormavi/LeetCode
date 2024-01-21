"""
You are given a sorted array consisting of only integers where every element appears
exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Approach: For each pair, first element takes even position
        # and second element takes odd position. This pattern will be
        # missed when single element is appeared in the array.

        # if mid is even, then it's duplicate should be in next index
        # or if mid is odd, then it's duplicate should be in previous index.

        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            # if any of the conditions is satisfied, then pattern is not missed,
            # so check in next half of the array
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 != 0 and nums[mid] == nums[mid - 1]):
                start = mid + 1
            else:
                end = mid
        return nums[start]

"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if
it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums is guaranteed to be rotated at some pivot.
    -10^4 <= target <= 10^4
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Approach: Same as search in rotated array but trick is to find the sorted half with duplicates
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            print("mid", mid)
            if nums[mid] == target:
                return True

            # If we cannot determine the sorted half because of duplicates
            # Different from search in rotated array
            if nums[start] == nums[mid]:
                start += 1
                continue

            # Approach: check progression is on which side so that target
            # can be searched in a range.
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

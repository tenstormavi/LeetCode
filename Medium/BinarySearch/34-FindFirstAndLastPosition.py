"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary Search -> O(log(n))
        def firstIndex(nums, target):
            startIndex = -1
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    startIndex = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return startIndex

        def lastIndex(nums, target):
            lastIndex = -1
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    lastIndex = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return lastIndex

        return [firstIndex(nums, target), lastIndex(nums, target)]

        # Two Pointers -> O(n)
        low = 0
        high = len(nums) - 1
        first, last = -1, -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                first = mid
                last = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [first, last]

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time
complexity and with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:
1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, si, mid, ei):
            # Compare and merge the two halves
            ans = []
            idx1 = si
            idx2 = mid + 1
            while idx1 <= mid and idx2 <= ei:
                if nums[idx1] < nums[idx2]:
                    ans.append(nums[idx1])
                    idx1 += 1
                else:
                    ans.append(nums[idx2])
                    idx2 += 1

            # Add the remaining items in either halves
            while idx1 <= mid:
                ans.append(nums[idx1])
                idx1 += 1

            while idx2 <= ei:
                ans.append(nums[idx2])
                idx2 += 1

            # Modify the original array i.e nums
            for i in ans:
                nums[si] = i
                si += 1

        def mergesort(nums, si, ei):
            # Base case
            if si >= ei:
                return

            mid = si + (ei - si) // 2

            mergesort(nums, si, mid)
            mergesort(nums, mid + 1, ei)
            merge(nums, si, mid, ei)

        # Approach - O(nlog(n)) - Merge Sort
        mergesort(nums, 0, len(nums) - 1)
        return nums

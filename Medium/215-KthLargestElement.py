"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution: Max heap
        heap = []
        for idx, num in enumerate(nums):
            heappush(heap, [-num, idx])

            if len(heap) > len(nums) + 1 - k:
                heappop(heap)

        return -1 * heap[0][0]

        # Solution: Min Heap
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

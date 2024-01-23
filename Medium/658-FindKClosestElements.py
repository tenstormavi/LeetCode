"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
    1 <= k <= arr.length
    1 <= arr.length <= 10^4
    arr is sorted in ascending order.
    -10^4 <= arr[i], x <= 10^4
"""

from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Solution -> Binary Search O(log(n))
        left = 0
        # if suppose right is the answer, we can't find any thing after right
        # mid will always land on left of the boundary
        right = len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]


        # Solution -> Heap O(nlog(n))
        heap = []
        for num in arr:
            distance = abs(num - x)
            if len(heap) < k:
                heappush(heap, (-1 * distance, num))
            else:
                if -1 * heap[0][0] > distance:
                    heappop(heap)
                    heappush(heap, (-1 * distance, num))
        return sorted([val for _, val in heap])


        # Solution -> O(n)
        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if abs(x - arr[left]) > abs(x - arr[right]):
                left = left + 1
            else:
                right = right - 1
        return arr[left:right+1]

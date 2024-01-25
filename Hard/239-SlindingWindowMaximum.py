"""
You are given an array of integers nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in the window. Each time
the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach: Since we have already calculated the max in a window, so while we
        # shifting one right we just have to calculate the new num with the largest of
        # last one.

        res = []
        q = deque()  # index
        left = right = 0

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # if left is out of bound, remove left val from window
            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1

            right += 1
        return res

        # Giving TLE: times we have to calculate k -> (n-k) times
        # Size of k is fixed so O(k * (n-k))
        # start = end = 0
        # ans = []
        # count = 1
        # while end < len(nums):
        #     while count == k:
        #         ans.append(max(nums[start:end+1]))
        #         start += 1
        #         count -= 1
        #     count += 1
        #     end += 1

        # return ans

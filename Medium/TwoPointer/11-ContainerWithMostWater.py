"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer approach: Try to find the max area based on heights
        # if left pointer is smaller, move left so that we can have potentially
        # greater height. Same for right pointer. In case of equal, any pointer
        # can be moved.
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
        return max_area

        # Brute Force - Find every possible container and calculate the area
        # and return the max ares among it
        # TLE
        # max_area = 0
        # hei = str(height)
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         width = j - i
        #         height = min(hei[i], hei[j])
        #         max_area = max(max_area, width * height)
        # return max_area

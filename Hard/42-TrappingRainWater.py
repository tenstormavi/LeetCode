"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # Base cases - 1 block, 2 blocks of different heights can't hold water
        # So we need blocks >= 3 to trap water
        # Blocks in desc/asc order can't trap water.

        # Calculate trap water -> min(maxLeft, maxRight) - currentHeight

        # Naive approach: Find the maxLeft and maxRight for each index and calculate the trap water - O(n^2)

        # Optimise: Pre-calculate the maxLeft and maxright - Time and Space -> O(n)

        if len(height) <= 2:
            return 0

        maxLeft = [0] * len(height)
        leftMax = height[0]
        for i in range(1, len(height)):
            # Calculate leftMax for all heights
            maxLeft[i] = leftMax
            leftMax = max(leftMax, height[i])

        maxRight = [0] * len(height)
        rightMax = height[-1]
        for i in range(len(height) - 2, -1, -1):
            # Calculate rightMax for all heights
            maxRight[i] = rightMax
            rightMax = max(rightMax, height[i])

        water = 0
        for i in range(1, len(height)):
            if height[i] < maxLeft[i] and height[i] < maxRight[i]:
                water += min(maxLeft[i], maxRight[i]) - height[i]
        return water

        # Solution 2 - Time O(n), Space O(1)
        if not height or len(height) <= 2:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]
        return water

"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in
the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it
does not fit in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1

Constraints:
    1 <= n <= 2^31 - 1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Approach: Just remember this logic
        # Step 1: Find the first point from backwards where number got decreased (deflection point).
        # Step 2: Find the just greater number from the deflection point going forward after the deflection point.
        # Step 3: Swap both the numbers (deflection and just greater)
        # Step 4: Sort the right half of the elements (after the deflection point)

        nums = list(str(n))
        i = len(nums) - 1

        # Step 1: Find the deflection point
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # No such integer exists
        if i == 0:
            return -1

        # Step 2: Find the just greater number from nums[idx]
        j = len(nums) - 1
        while j > i - 1 and nums[j] <= nums[i - 1]:
            j -= 1

        # Step 3: Swap the numbers
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Step 4: Sort the right half of the list
        nums[i:] = nums[i:][::-1]

        res = int("".join(nums))

        return res if res < 2 ** 31 else -1

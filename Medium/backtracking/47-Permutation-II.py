"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations
in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Approach: Normal decision tree will not work as it will create duplicates
        # Use a map to remove the duplciates while creating the path
        def solve(path): # TC - O(N)
            # Base case
            if len(path) == len(nums):
                res.append(path)
                return

            for key in map:
                if map[key] > 0:
                    map[key] -= 1
                    solve(path + [key])
                    map[key] += 1

        res = []
        map = Counter(nums)
        path = []
        solve(path)
        return res

        # Approach: Same as permutation(46), just skip the duplicates..
        # At each place each element will be there by swapping the elements
        def solve(nums, idx):
            # Base case
            if idx >= len(nums) and nums[:] not in res: # don't append duplicates
                if nums[:] in res:
                    return
                # note [:] make a deep copy since otherwise we'd be appended the same list over and over
                res.append(nums[:])
                return

            for j in range(idx, len(nums)):
                nums[idx], nums[j] = nums[j], nums[idx]
                solve(nums, idx + 1)
                # backtrack
                nums[idx], nums[j] = nums[j], nums[idx]

        res = []
        idx = 0
        solve(nums, idx)
        return res

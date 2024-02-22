"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach: At each place each element will be there by swapping the elements - (preferred)
        def solve(nums, idx):
            # Base case
            if idx >= len(nums):
                # note [:] make a deep copy since otherwise we'd be append the same list over and over
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

        # Approach: Combinational search problem, use Backtracking template
        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, num in enumerate(nums):
                # skip used letters
                if used[i]:
                    continue

                # add letter to permutation and mark letter as used
                path.append(num)
                used[i] = True

                dfs(path, used)

                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False

        res = []
        dfs([], [False] * len(nums))
        return res


        # Approach: Map can also be used to get the permutation
        res = []

        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path + [x])
                    counter[x] += 1

        dfs(Counter(nums), [])
        return res

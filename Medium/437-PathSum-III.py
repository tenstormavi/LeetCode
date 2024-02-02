"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the
sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go
downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
    The number of nodes in the tree is in the range [0, 1000].
    -10^9 <= Node.val <= 10^9
    -1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Approach: https://medium.com/geekculture/path-sum-iii-leetcode-437-588d8e56acac
        # To find all the paths whose sum is equals to target we need to consider all possible paths
        # in the tree which arises from parent to child nodes. Most basic approach would be by considering
        # each node as a root node and calculate sum of paths from this node. But there are a lot of
        # repetitive operations, so we can use prefix_sum to mitigate that.

        self.count = 0
        cur_sum = 0
        sum_map = defaultdict(int)

        def traverseTree(root, cur_sum):
            if not root:
                return

            cur_sum += root.val

            if cur_sum == targetSum:
                self.count += 1

            if sum_map.get(cur_sum - targetSum):
                self.count += sum_map[cur_sum - targetSum]

            sum_map[cur_sum] += 1

            traverseTree(root.left, cur_sum)
            traverseTree(root.right, cur_sum)

            if sum_map.get(cur_sum):
                sum_map[cur_sum] -= 1

        traverseTree(root, cur_sum)
        return self.count

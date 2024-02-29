"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not
matter the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100
"""
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution: Using hashmap
        def recurse(node):
            if not node:
                return -1

            left = recurse(node.left)
            right = recurse(node.right)

            level = max(left, right) + 1

            res[level].append(node.val)
            return level

        res = defaultdict(list)
        recurse(root)
        return res.values()

        # Solution:
        def recurse(node):
            # When we read the leaf return -1 (to help start our levels
            # at 0 - because we add 1 when returned).
            if not node:
                return -1

            # find the height of the l and r subtrees.
            left = recurse(node.left)
            right = recurse(node.right)

            level = max(left, right) + 1

            # If we haven't visited a level, append to the results.
            if len(res) <= level:
                res.append([])

            res[level].append(node.val)
            return level

        res = []
        recurse(root)
        return res

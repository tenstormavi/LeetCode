"""
Given the root of a binary search tree and an integer k, return true if there exist two elements
in the BST such that their sum is equal to k, or false otherwise.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -10^4 <= Node.val <= 10^4
    root is guaranteed to be a valid binary search tree.
    -10^5 <= k <= 10^5
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # BFS -> level-order
        if not root:
            return False

        seen = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                if node.val in seen:
                    return True
                else:
                    seen.add(k - node.val)
                queue.append(node.left)
                queue.append(node.right)
        return False

        # DFS -> Pre-order
        if not root:
            return False

        stack = [root]
        seen = set()
        target = k
        while stack:
            node = stack.pop()
            if node:
                if node.val in seen:
                    return True
                else:
                    seen.add(target - node.val)
                stack.append(node.right)
                stack.append(node.left)
        return False

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Solution 1
        stack = []
        if root:
            stack.append([root.left, root.right])

        while stack:
            left, right = stack.pop()
            if left and right:
                if left.val != right.val:
                    return False
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            elif left or right:
                return False
        return True

        # Solution 2
        if root is None:
            return True
        queue = [root, root]
        while queue:
            root1 = queue.pop()
            root2 = queue.pop()

            if root1 is None and root2 is None:
                return True
            if root1.val == root2.val:
                if root1.left is not None and root2.right is not None:
                    queue.insert(0, root1.left)
                    queue.insert(0, root2.right)
                elif root1.left is None and root2.right is None:
                    pass
                elif root1.left is None or root2.right is None:
                    return False
                if root1.right is not None and root2.left is not None:
                    queue.insert(0, root1.right)
                    queue.insert(0, root2.left)
                elif root1.right is None and root2.left is None:
                    pass
                elif root1.right is None or root2.left is None:
                    return False
            else:
                return False
        return True

        # Solution 3 - Recursive
        def checkMirror(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is not None and root2 is None or root1 is None and root2 is not None:
                return False

            if root1.val == root2.val:
                return checkMirror(root1.left, root2.right) and checkMirror(root1.right, root2.left)

        return checkMirror(root, root)

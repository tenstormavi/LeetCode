"""
Given the root of a binary tree, flatten the tree into a "linked list":
    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in
    the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Solution -> Morris Traversal. Space complexity - O(1)
        cur = root
        while cur:
            if cur.left:
                left = cur.left        # get the left subtree of cur
                right = cur.right      # get the right subtree of cur
                cur.left = None        # cur's left subtree set to be None
                cur.right = left       # switch the left subtree to the right subtree
                while left.right:      # get the far-rigth leaf of the left subtree
                    left = left.right
                left.right = right     # put the right subtree of cur as the right subtree of the far-right leaf
            cur = cur.right

        # Solution 1: (easy to understand) -> Time and Space complexity - O(n)
        def dfs(cur):
            if not cur:
                return None
            if self.prev:
                self.prev.left = None
                self.prev.right = cur
            next = cur.right
            self.prev = cur
            dfs(cur.left)
            dfs(next)

        self.prev = None
        dfs(root)

        # Solution 2: Time and Space complexity - O(n)
        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            return rightTail or leftTail or root

        dfs(root)

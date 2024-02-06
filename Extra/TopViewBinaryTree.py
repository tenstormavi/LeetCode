"""
Given below is a binary tree. The task is to print the top view of binary tree.
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
"""

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import deque


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):

        # code here
        if not root:
            return

        queue = deque()
        queue.append((root, 0))
        mp = {}

        while queue:
            root, hd = queue.popleft()
            if hd not in mp:
                mp[hd] = root.data

            if root.left:
                queue.append((root.left, hd - 1))
            if root.right:
                queue.append((root.right, hd + 1))

        res = []
        for i in sorted(mp):
            res.append(mp[i])

        return res

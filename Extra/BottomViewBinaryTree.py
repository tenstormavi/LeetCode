"""
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
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
    def bottomView(self, root):

        # code here
        if not root:
            return

        queue = deque()
        queue.append((root, 0))
        mp = {}

        while queue:
            root, hd = queue.popleft()
            mp[hd] = root.data # Only this line is changes from top view

            if root.left:
                queue.append((root.left, hd - 1))
            if root.right:
                queue.append((root.right, hd + 1))

        res = []
        for i in sorted(mp):
            res.append(mp[i])

        return res

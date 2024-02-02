"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
the sum of the node values in the path equals targetSum. Each path should be returned as a list
of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a
node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Iterative solution -> Queue (DFS)
        if not root:
            return []

        path = []
        queue = [(root, root.val, [root.val])]

        while queue:
            cur, cur_sum, temp_path = queue.pop(0)

            if not cur.left and not cur.right and cur_sum == targetSum:
                path.append(temp_path)

            if cur.left:
                queue.append((cur.left, cur_sum + cur.left.val, temp_path + [cur.left.val]))

            if cur.right:
                queue.append((cur.right, cur_sum + cur.right.val, temp_path + [cur.right.val]))
        return path

        # Iterative solution -> stack (BFS)
        if not root:
            return []

        path = []
        stack = [(root, targetSum - root.val, [root.val])]

        while stack:
            cur, cal_sum, cur_path = stack.pop()

            if not cur.left and not cur.right and cal_sum == 0:
                path.append(cur_path)

            if cur.right:
                stack.append((cur.right, cal_sum - cur.right.val, cur_path + [cur.right.val]))
            if cur.left:
                stack.append((cur.left, cal_sum - cur.left.val, cur_path + [cur.left.val]))
        return path

        # Recursive solution 2
        def dfs(root, targetSum, path, temp):
            if root:
                if not root.left and not root.right and targetSum == root.val:
                    temp.append(root.val)
                    path.append(temp)

                dfs(root.left, targetSum - root.val, path, temp + [root.val])
                dfs(root.right, targetSum - root.val, path, temp + [root.val])

        path = []
        dfs(root, targetSum, path, [])
        return path

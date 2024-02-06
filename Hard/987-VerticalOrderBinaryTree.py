"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each
column index starting from the leftmost column and ending on the rightmost column. There may
be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Use a dictionary where keys are (x, y) tuples and values are lists of node values
        node_map = defaultdict(list)
        # Queue for BFS: ((node, x distance, y level))
        queue = deque([(root, 0, 0)])

        while queue:
            node, x, y = queue.popleft()
            node_map[(x, y)].append(node.val)

            # Enqueue children with updated coordinates
            if node.left:
                queue.append((node.left, x - 1, y + 1))
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        # node_map eg - {(0, 0): [1], (-1, 1): [2], (1, 1): [3], (-2, 2): [4], (0, 2): [6, 5], (2, 2): [7]}

        # Sort the nodes first by x coordinate, then by y coordinate, and sort the values if needed
        sorted_nodes = sorted(node_map.items(), key=lambda item: (item[0][0], item[0][1]))
        # sorted_nodes - [((-2, 2), [4]), ((-1, 1), [2]), ((0, 0), [1]), ((0, 2), [6, 5]), ((1, 1), [3]), ((2, 2), [7])]

        # Prepare the output, ensuring values with the same (x, y) are sorted
        output_map = defaultdict(list)
        for (x, y), values in sorted_nodes:
            for value in sorted(values):  # Sort values if there are multiple nodes in the same position
                output_map[x].append(value)

        # eg - [[4], [2], [1, 5, 6], [3], [7]]
        return [output_map[x] for x in output_map]

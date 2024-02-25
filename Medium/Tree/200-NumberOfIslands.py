"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # TC - O(N)
        # 0 - water, 1 - land, 2- visited land

        def mark_island(grid, i, j, row, col):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != "1":
                return

            # mark visited
            grid[i][j] = "2"

            # Mark in all four direction recursively
            mark_island(grid, i + 1, j, row, col)
            mark_island(grid, i - 1, j, row, col)
            mark_island(grid, i, j + 1, row, col)
            mark_island(grid, i, j - 1, row, col)

        island = 0
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    island += 1
                    mark_island(grid, i, j, row, col)
        return island

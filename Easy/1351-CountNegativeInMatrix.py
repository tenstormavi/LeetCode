"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100

Follow up: Could you find an O(n + m) solution?
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Solution: Using both sorted rows and column -> O(n+m)
        col_size = len(grid[0])
        col = 0
        row = len(grid) - 1
        count = 0
        while row >= 0 and col < col_size:
            if grid[row][col] < 0:
                count += col_size - col
                row -= 1
            else:
                col += 1
        return count

        # Solution: Only using sorting rows, Binary Search -> O(mlog(n))
        def binarySearch(row):
            low, high = 0, len(row)
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] < 0:
                    high = mid
                else:
                    low = mid + 1
            return len(row) - low

        count = 0
        for row in grid:
            count += binarySearch(row)
        return count

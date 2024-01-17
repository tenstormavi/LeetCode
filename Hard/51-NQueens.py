"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
    1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # for tracking the columns which already have a queen
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)
        res = []
        board = [["."] * n for i in range(n)]  # start with empty board

        def backtrack(r):
            if r == n:
                dup = ["".join(row) for row in board]
                res.append(dup)
                return

            for c in range(n):
                # If the current square doesn't have another queen in same column and diagonal.
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"  # place the queen

                backtrack(r + 1)

                # reset the path
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

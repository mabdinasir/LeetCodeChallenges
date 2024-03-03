# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(i - row) == abs(board[i] - col):
                    return False
            return True
        
        def backtrack(board, row):
            if row == n:
                res.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1
        res = []
        board = [-1] * n
        backtrack(board, 0)
        return res
    
sol = Solution()
n = 4
print(sol.solveNQueens(n)) # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] or [["..Q.","Q...","...Q",".Q.."],[".Q..","...Q","Q...","..Q."]]

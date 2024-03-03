# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(i - row) == abs(board[i] - col):
                    return False
            return True
        
        def backtrack(board, row):
            if row == n:
                nonlocal count
                count += 1
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1
        count = 0
        board = [-1] * n
        backtrack(board, 0)
        return count
    
sol = Solution()
n = 4
print(sol.totalNQueens(n)) # Output: 2
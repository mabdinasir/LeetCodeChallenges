# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidRow(board, i):
                return False
            if not self.isValidCol(board, i):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidBox(board, i, j):
                    return False
        return True
    
    def isValidRow(self, board: List[List[str]], row: int) -> bool:
        nums = set()
        for i in range(9):
            if board[row][i] != '.':
                if board[row][i] in nums:
                    return False
                nums.add(board[row][i])
        return True
    
    def isValidCol(self, board: List[List[str]], col: int) -> bool:
        nums = set()
        for i in range(9):
            if board[i][col] != '.':
                if board[i][col] in nums:
                    return False
                nums.add(board[i][col])
        return True
    
    def isValidBox(self, board: List[List[str]], row: int, col: int) -> bool:
        nums = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                if board[i][j] != '.':
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])
        return True
    
print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) # True
print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) # False
print(Solution().isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]])) # False
print(Solution().isValidBox([[1,2,3],[4,5,6],[7,8,9]], 0, 0)) # True
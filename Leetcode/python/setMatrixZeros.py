# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        
        firstRowHasZero = False
        firstColHasZero = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstColHasZero = True
                break
        
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowHasZero = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRowHasZero:
            for j in range(n):
                matrix[0][j] = 0
        
        if firstColHasZero:
            for i in range(m):
                matrix[i][0] = 0

    def printMatrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print(row)

sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
sol.printMatrix(matrix) # [[1,0,1],[0,0,0],[1,0,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
sol.printMatrix(matrix) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
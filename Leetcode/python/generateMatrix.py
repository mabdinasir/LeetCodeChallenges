# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        num = 1
        while num <= n*n:
            for i in range(left, right+1):
                result[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom+1):
                result[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left-1, -1):
                result[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result

sol = Solution()
n = 3
print(sol.generateMatrix(n)) # Output: [[1,2,3],[8,9,4],[7,6,5]]
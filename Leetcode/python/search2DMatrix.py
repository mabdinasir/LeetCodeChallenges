# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            midElement = matrix[mid // n][mid % n]
            if midElement == target:
                return True
            elif midElement < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

from typing import List

class Solution:
    def generate(self, numRows: int) -> list[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    row.append(res[i-1][j-1] + res[i-1][j])
                row.append(1)
                res.append(row)
            return res

print(Solution().generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
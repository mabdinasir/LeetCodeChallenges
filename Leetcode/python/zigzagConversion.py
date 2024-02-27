# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * numRows
        i = 0
        flag = -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return ''.join(res)

s = Solution()
print(s.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
print(s.convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
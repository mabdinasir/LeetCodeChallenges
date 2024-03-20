# This is a left aligned triangle pattern
# Here is the pattern for n = 5

class Solution:
    def leftAlignedTriangle(self, n):
        for i in range(n):
            print(i, '*' * i)
        return

# Test
s = Solution()
s.leftAlignedTriangle(5)
# Output: 
# 0
# 1 *
# 2 **
# 3 ***
# 4 ****
# 5 *****

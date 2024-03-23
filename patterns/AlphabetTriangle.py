# This is an alphabet triangle pattern.
# Output:
# Output:
# E D C B A
#  D C B A
#   C B A
#    B A
#     A

class Solution:
    def alphabetTriangle(self, n):
        for i in range(n, 0, -1):
            for j in range(i, 0, -1):
                print(chr(64 + j), end=' ')
            print()
        return

# Test
s = Solution()
s.alphabetTriangle(5)

# Output:
# E D C B A
#  D C B A
#   C B A
#    B A
#     A


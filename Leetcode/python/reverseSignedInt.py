# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = -int(str(-x)[::-1])
        else:
            res = int(str(x)[::-1])
        return res if -2**31 <= res <= 2**31 - 1 else 0

s = Solution()
print(s.reverse(123)) # 321
print(s.reverse(-123)) # -321
print(s.reverse(120)) # 21
print(s.reverse(0)) # 0
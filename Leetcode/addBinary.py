# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution(object):
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = ""
        i = 0
        while i < len(a) or i < len(b):
            if i < len(a):
                carry += int(a[i])
            if i < len(b):
                carry += int(b[i])
            result += str(carry % 2)
            carry = carry // 2
            i += 1
        if carry:
            result += str(carry)
        return result[::-1]
    

print(Solution().addBinary("11", "1")) # "100"
print(Solution().addBinary("1010", "1011")) # "10101"
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiplyStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return ''.join(map(str, result[::-1]))
    
    def simpleMultiplyStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
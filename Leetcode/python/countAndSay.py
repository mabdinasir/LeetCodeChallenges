# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":


# Given a positive integer n, return the nth term of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        res = ""
        count = 1
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                res += str(count) + prev[i - 1]
                count = 1
        res += str(count) + prev[-1]
        return res
    
# Time complexity: O(2^n)
# Space complexity: O(2^n)
# Example 1:
n = 1
# Output: "1"
print(Solution().countAndSay(n))

# Example 2:
n = 4
# Output: "1211"
print(Solution().countAndSay(n))


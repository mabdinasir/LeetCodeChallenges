
# Code
# Testcase
# Test Result
# Test Result
# 12. Integer to Roman
# Medium
# Topics
# Companies
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        while num > 0:
            if num >= 1000:
                roman += "M"
                num -= 1000
            elif num >= 900:
                roman += "CM"
                num -= 900
            elif num >= 500:
                roman += "D"
                num -= 500
            elif num >= 400:
                roman += "CD"
                num -= 400
            elif num >= 100:
                roman += "C"
                num -= 100
            elif num >= 90:
                roman += "XC"
                num -= 90
            elif num >= 50:
                roman += "L"
                num -= 50
            elif num >= 40:
                roman += "XL"
                num -= 40
            elif num >= 10:
                roman += "X"
                num -= 10
            elif num >= 9:
                roman += "IX"
                num -= 9
            elif num >= 5:
                roman += "V"
                num -= 5
            elif num >= 4:
                roman += "IV"
                num -= 4
            else:
                roman += "I"
                num -= 1
        return roman

print(Solution().intToRoman(3567)) # "III"
print(Solution().intToRoman(4)) # "IV"
print(Solution().intToRoman(9)) # "IX"
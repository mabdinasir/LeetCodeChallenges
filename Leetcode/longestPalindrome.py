# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i + 1)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest

print(Solution().longestPalindrome("babad")) # bab
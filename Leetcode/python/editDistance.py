# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

# Approach:
# We will use dynamic programming to solve this problem.
# We will create a 2D array of size m+1 and n+1 where m and n are the lengths of the two strings.
# We will initialize the first row and column with the values from 0 to m and 0 to n.
# We will then iterate through the array and fill the values using the following logic: 
# if the characters at the current index are the same, we will take the value from the previous diagonal cell.
# If the characters are different, we will take the minimum of the previous row, column, and diagonal cell and add 1 to it.
# The value at the last cell will be the minimum number of operations required to convert word1 to word2.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[m][n]

print(Solution().minDistance("horse", "ros")) # 3
print(Solution().minDistance("intention", "execution")) # 5

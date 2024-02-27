# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, s: int) -> list[str]:
        def backtrack(s, left, right, path):
            if len(path) == 2 * s:
                combinations.append(''.join(path))
                return
            if left < s:
                path.append('(')
                backtrack(s, left + 1, right, path)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(s, left, right + 1, path)
                path.pop()
        combinations = []
        backtrack(s, 0, 0, [])
        return combinations

print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(1)) # ["()"]
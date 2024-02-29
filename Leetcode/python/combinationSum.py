# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

# Approach:
# 1. We will use backtracking to solve this problem.
# 2. We will start with an empty list and keep adding elements to the list until the sum of the list is equal to the target.
# 3. If the sum of the list is greater than the target, we will return.
# 4. If the sum of the list is equal to the target, we will add the list to the result.
# 5. We will iterate through the candidates and call the function recursively with the updated target and list.
# 6. We will remove the last element from the list after the recursive call to backtrack.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, target, path):
            if target < 0:
                return
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])
        backtrack(0, target, [])
        return result
    
s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
print(s.combinationSum([2], 1))
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
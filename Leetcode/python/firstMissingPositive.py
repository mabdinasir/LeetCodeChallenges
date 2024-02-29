# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
    
s = Solution()
nums = [1,2,0]
print(s.firstMissingPositive(nums)) # 3

nums = [3,4,-1,1]
print(s.firstMissingPositive(nums)) # 2

nums = [7,8,9,11,12]
print(s.firstMissingPositive(nums)) # 1
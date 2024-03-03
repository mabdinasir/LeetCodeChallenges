# Given an integer array nums, find the subarray with the largest sum, and return its sum.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    def printEachSubArrayWithTotal(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print(nums[i:j+1], sum(nums[i:j+1]))

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums)) # Output: 6 

sol.printEachSubArrayWithTotal(nums) # Output:   [-2] -2
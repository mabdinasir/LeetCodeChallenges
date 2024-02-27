# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest

print(Solution().threeSumClosest([-1,2,1,-4], 1)) # 2
print(Solution().threeSumClosest([1,1,1,0], -100)) # 2
print(Solution().threeSumClosest([1,1,1,0], 100)) # 3
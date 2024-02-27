# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        if nums[0] < nums[-1]:
            return self.binarySearch(nums, target, 0, len(nums)-1)
        pivot = self.findPivot(nums, 0, len(nums)-1)
        if target >= nums[0]:
            return self.binarySearch(nums, target, 0, pivot)
        else:
            return self.binarySearch(nums, target, pivot+1, len(nums)-1)

    def findPivot(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return start
        if start + 1 == end:
            return start if nums[start] > nums[end] else end
        mid = (start + end) // 2
        if nums[mid] > nums[start]:
            return self.findPivot(nums, mid, end)
        else:
            return self.findPivot(nums, start, mid)

    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binarySearch(nums, target, start, mid-1)
        else:
            return self.binarySearch(nums, target, mid+1, end)

print(Solution().search([4,5,6,7,0,1,2], 0)) # 4
print(Solution().search([4,5,6,7,0,1,2], 3)) # -1
print(Solution().search([1], 0)) # -1
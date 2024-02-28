# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        if len(nums) == 2:
            if nums[0] == target and nums[1] == target:
                return [0, 1]
            elif nums[0] == target:
                return [0, 0]
            elif nums[1] == target:
                return [1, 1]
            else:
                return [-1, -1]
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

    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> List[int]:
        if start > end:
            return [-1, -1]
        mid = (start + end) // 2
        if nums[mid] == target:
            left = mid
            right = mid
            while left > 0 and nums[left-1] == target:
                left -= 1
            while right < len(nums)-1 and nums[right+1] == target:
                right += 1
            return [left, right]
        if nums[mid] > target:
            return self.binarySearch(nums, target, start, mid-1)
        else:
            return self.binarySearch(nums, target, mid+1, end)

print(Solution().searchRange([5,7,7,8,8,10], 8)) # [3, 4]
print(Solution().searchRange([5,7,7,8,8,10], 6)) # [-1, -1]

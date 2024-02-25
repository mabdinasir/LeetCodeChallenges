# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
    def printTree(self, root: Optional[TreeNode]) -> None:
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

sol = Solution()
sol.printTree(sol.sortedArrayToBST([-10,-3,0,5,9]))
sol.printTree(sol.sortedArrayToBST([1,3]))
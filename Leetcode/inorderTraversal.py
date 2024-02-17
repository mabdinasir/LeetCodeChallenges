# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
        
    def printList(self, list):
        for i in list:
            print(i, end = " ")
        print()

# Test cases
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
sol = Solution()
sol.printList(sol.inorderTraversal(root)) # [1, 3, 2]
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        if root is None:
            return True
        return self.isSymmetricTree(root.left, root.right)
    
    def isSymmetricTree(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetricTree(left.left, right.right) and self.isSymmetricTree(left.right, right.left)
    
p = TreeNode(1, TreeNode(2), TreeNode(2))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print(Solution().isSymmetric(p)) # True
print(Solution().isSymmetric(q)) # False

# Input: root = [1,2,2,3,4,4,3]
# Output: true

p2 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(Solution().isSymmetric(p2)) # True

# root = [1,2,2,null,3,null,3]
# Output: false
p3 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(Solution().isSymmetric(p3)) # False
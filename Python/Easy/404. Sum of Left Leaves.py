# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, 0) if root else 0 
    
    def dfs(self, root, count):
        if not root:
            return 
        if root.left and not root.left.left and not root.left.right:
            count += root.left.val
        
        if root.left:
            count = self.dfs(root.left, count)
        if root.right:
            count = self.dfs(root.right, count)
            
        return count
        
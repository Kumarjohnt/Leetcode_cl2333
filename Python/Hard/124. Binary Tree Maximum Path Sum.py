# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def recursive(root):
            if not root:
                return (0,  -float('inf'))
            
            left, left_max = recursive(root.left)
            right, right_max = recursive(root.right)
            
            max_val = max(left_max, right_max, left + right + root.val, root.val + left, root.val + right, root.val)
            
            return (max(root.val, root.val + left, root.val + right), max_val)
        
        return recursive(root)[1]
            
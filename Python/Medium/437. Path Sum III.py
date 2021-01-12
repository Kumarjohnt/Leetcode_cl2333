# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        memo = {0: 1}

        
        def find(root, target, cur_sum):
            if not root:
                return 0
            
            cur_sum = cur_sum + root.val
            cur_res = memo.get(cur_sum - target, 0)
            memo[cur_sum] = memo.get(cur_sum, 0) + 1
            res = cur_res + find(root.left, target, cur_sum) + find(root.right, target, cur_sum)
            memo[cur_sum] -= 1
            return res
            
        return find(root, sum, 0)
        
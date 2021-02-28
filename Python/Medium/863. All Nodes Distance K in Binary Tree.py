# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return None
        
        d = defaultdict(list)
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                d[node.val].append(node.left.val)
                d[node.left.val].append(node.val)
            if node.right:
                q.append(node.right)
                d[node.val].append(node.right.val)
                d[node.right.val].append(node.val)

        q = deque([target.val])
        visited = set([target.val])
        while K>0:
            for i in range(len(q)):
                val = q.popleft()
                for v in d[val]:
                    if v in visited:
                        continue
                    q.append(v)
                    visited.add(v)
            K -= 1
        
        return list(q)
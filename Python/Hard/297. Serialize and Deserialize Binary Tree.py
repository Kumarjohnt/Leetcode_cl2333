# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        
        res = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if node:
                res += "," + str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += ",None"
        
        return res
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        """
        if not data:
            return None
        
        data = data.split(",")
        data = deque(data)
        _, val = data.popleft(), data.popleft()
        root = None if val is None else TreeNode(int(val))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                left, right = data.popleft(), data.popleft()
                left = None if left == 'None' else TreeNode(int(left))
                right = None if right == 'None' else TreeNode(int(right))
                node.left, node.right = left, right
                queue.extend([left, right])
        
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
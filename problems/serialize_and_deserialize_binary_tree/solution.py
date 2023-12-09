# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    NULL = '#'
    SEP = ','

    def _serialize(self, root, serialized: List[str]):
        if not root:
            serialized.append(self.NULL)
            return
        
        self._serialize(root.left, serialized)
        self._serialize(root.right, serialized)

        serialized.append(str(root.val))
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        
        self._serialize(root, serialized)

        return self.SEP.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        return self._deserialize(deque(data.split(self.SEP)))
    
    def _deserialize(self, nodes):
        if not nodes:
            return None
        
        if nodes[-1] == self.NULL:
            nodes.pop()
            return None
        
        root = TreeNode(val=nodes.pop())
        root.right = self._deserialize(nodes)
        root.left = self._deserialize(nodes)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
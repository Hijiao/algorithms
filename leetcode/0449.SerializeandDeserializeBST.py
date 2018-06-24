# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import json
class Codec:
    def __init__(self):
        self.node_dict ={}

    def walk_through(self,num,node):
        self.node_dict[num] =node.val
        if node.left:
            self.walk_through(num<<1,node.left)
        if node.right:
            self.walk_through((num<<1)+1,node.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root:
            self.walk_through(1,root)
        return json.dumps(self.node_dict)

    def de_node(self,num):
        if str(num) in self.node_dict:
            node = TreeNode(self.node_dict[str(num)])
            node.left = self.de_node(num<<1)
            node.right = self.de_node((num<<1)+1)
            return node
        else:
            return None

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.node_dict = json.loads(data)
        return self.de_node(1)


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right =right
# Your Codec object will be instantiated and called as such:
codec = Codec()
# print codec.serialize(root)
root = codec.deserialize(codec.serialize(root))
print root.left.val
print root.right.val
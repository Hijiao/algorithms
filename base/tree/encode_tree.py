# -*- coding:utf-8 -*-
import json


# https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=13&tqId=11214&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# 序列化二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def encodeNode(self, node, index, treedict):
        treedict[index] = node.val
        left_child_index = index << 1
        if node.left is not None:
            self.encodeNode(node.left, left_child_index, treedict)
        if node.right is not None:
            self.encodeNode(node.right, left_child_index + 1, treedict)

    def decodeNode(self, index, value, treedict):
        node = TreeNode(value)
        left_index = index << 1
        if treedict.get(str(left_index)) is not None:
            node.left = self.decodeNode(left_index, treedict[str(left_index)], treedict)
        right_index = left_index + 1
        if treedict.get(str(right_index)) is not None:
            node.right = self.decodeNode(right_index, treedict[str(right_index)], treedict)
        return node

    def Serialize(self, root):
        treedict = {}
        if root is not None:
            self.encodeNode(root, 1, treedict)
        return json.dumps(treedict)
        # write code here

    def Deserialize(self, s):
        treedict = json.loads(s)
        if treedict.get('1') is None:
            return None
        else:
            root = self.decodeNode(1, treedict[str(1)], treedict)
        return root
        # write code here


root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')

s = Solution().Serialize(root)
print s

r = Solution().Deserialize(s)
print "r", r.val
print "r.left", r.left.val
print "R.RIGHT", r.right.val

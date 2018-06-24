# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        firsts = root.val
        level = [root]
        while level:
            firsts = level[0].val
            for i in range(len(level)):
                node = level.pop(0)
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
        return firsts

root = TreeNode(2)
root.left =TreeNode(1)
root.right= TreeNode(3)

print Solution().findBottomLeftValue(root)
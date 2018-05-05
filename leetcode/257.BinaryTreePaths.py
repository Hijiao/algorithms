# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        path = []
        self.pre_order(root, path, result)
        return result

    def pre_order(self, root, path, result):
        path = path[:] + [str(root.val)]

        if root.left is None and root.right is None:
            result.append('->'.join(path))
        if root.left is not None:
            self.pre_order(root.left, path, result)
        if root.right is not None:
            self.pre_order(root.right, path, result)




root =TreeNode(1)
root.left =TreeNode(2)
root.right = TreeNode(3)
root.left.right=TreeNode(5)

print Solution().binaryTreePaths(root)


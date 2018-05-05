class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys


class Solution(object):
    def __init__(self):
        self.INF = 2 ** 32
        self.pre_val = - sys.maxint
        self.min_diff = sys.maxint

    def getMinimumDifference2(self, root):
        self.in_order(root)
        return self.min_diff

    def in_order(self, root):
        if root is None:
            pass
        else:
            self.in_order(root.left)
            if root.val - self.pre_val < self.min_diff:
                self.min_diff = root.val - self.pre_val
                self.pre_val = root.val
            self.in_order(root.right)


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return min(self.check(root), self.getMinimumDifference(root.left) if root.left is not None else self.INF,
                   self.getMinimumDifference(root.right) if root.right is not None else self.INF)

    def check(self, root):
        if root is None:
            return self.INF

        bigger = self.getMinBigger(root)
        smaller = self.getMaxSmaller(root)
        m = min(bigger - root.val if bigger is not None else self.INF,
                root.val - smaller if smaller is not None else self.INF)
        # print root.val, bigger, smaller, m
        return m

    def getMinBigger(self, root):
        if root.right is None:
            return None
        else:
            root = root.right

        while root.left is not None:
            root = root.left
        return root.val

    def getMaxSmaller(self, root):
        if root.left is None:
            return None
        else:
            root = root.left
        while root.right is not None:
            root = root.right
        return root.val


root = TreeNode(1476)
root.left = TreeNode(1054)
root.left.left = TreeNode(1)
root.left.left.right = TreeNode(215)
root.left.left.right.right = TreeNode(745)

print Solution().getMinimumDifference(root)


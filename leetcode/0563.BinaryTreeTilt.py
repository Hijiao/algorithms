# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.total_tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def order(root):
            if root is None:
                return 0
            sum_left = order(root.left)
            sum_right = order(root.right)
            if sum_left > sum_right:
                self.total_tilt += sum_left - sum_right
            else:
                self.total_tilt += sum_right - sum_left
            return sum_left + sum_right + root.val

        order(root)
        return self.total_tilt


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print  Solution().findTilt(root)

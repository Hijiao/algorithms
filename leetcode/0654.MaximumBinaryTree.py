# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = None
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            if root is None:
                root = node
            elif root.val < node.val:
                node.left = root
                root = node
                # root = node
            elif root.val > node.val:
                p = root
                while (p.right is not None and p.right.val > node.val):
                    p = p.right
                if p.right is not None:
                    node.left = p.right
                    p.right = node
                else:
                    p.right = node
        return root


def level_order(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val if node is not None else "null")
        if node is not None:
            queue.append(node.left)
            queue.append(node.right)


tree = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
level_order(tree)

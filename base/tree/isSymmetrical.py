# -*- coding:utf-8 -*-
# https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# 是否是镜像树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True

        def areSymmetricalNodes(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is not None and n2 is not None:
                return n1.val ==n2.val and areSymmetricalNodes(n1.right, n2.left) and areSymmetricalNodes(n1.left, n2.right)
            return False

        return areSymmetricalNodes(pRoot.left, pRoot.right)

        # write code here
        # mirror_flag = True
        # continue_flag = True
        # queue = [pRoot.left, pRoot.right]
        #
        # while mirror_flag and continue_flag:
        #     continue_flag = False
        #     size = len(queue)
        #     if size % 2 == 1:
        #         return False
        #     for i in range(size / 2):
        #         if queue[i] is None and queue[size - 1 - i] is None:
        #             continue
        #         if queue[i] is None or queue[size - 1 - i] is None:
        #             return False
        #
        #         if queue[i].val != queue[size - 1 - i].val:
        #             return False
        #
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if node is not None:
        #             continue_flag = True
        #             queue.append(node.left)
        #             queue.append(node.right)
        #         else:
        #             queue.append(None)
        #             queue.append(None)
        # return mirror_flag

    def areSymmetrical(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is not None and n2 is not None:
            return self.areSymmetrical(n1.right, n2.left) and self.areSymmetrical(n1.left, n2.right)
        return False


# root = TreeNode(8)
# root.left = TreeNode(6)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(7)
#
# root.right = TreeNode(6)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(5)
#
# print  Solution().isSymmetrical(root)

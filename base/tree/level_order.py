# -*- coding:utf-8 -*-

# https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288?tpId=13&tqId=11213&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def level_order(self, root):
        pass

    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        queue1 = [pRoot]
        queue2 = []
        result = []
        cur_level = []
        while len(queue1) > 0 or len(queue2) > 0:
            while len(queue1) > 0:
                node = queue1.pop(0)
                cur_level.append(node.val)
                if node.left is not None:
                    queue2.append(node.left)
                if node.right is not None:
                    queue2.append(node.right)
            if len(cur_level) > 0:
                result.append(cur_level)
                cur_level = []

            while queue2:
                node = queue2.pop(0)
                cur_level.append(node.val)
                if node.left is not None:
                    queue1.append(node.left)
                if node.right is not None:
                    queue1.append(node.right)
            if len(cur_level) > 0:
                result.append(cur_level)
                cur_level = []
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print Solution().Print(root)

# coding =utf-8
# 剑指offer 面试题30 包含min函数的栈
# https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# https://leetcode.com/problems/min-stack/description/

class Solution:
    def __init__(self):
        self.s = []

    def push(self, node):
        if not self.s:
            self.s.append((node, node))
        else:
            last_min = self.s[-1][1]
            new_min = min(last_min, node)
            self.s.append((node, new_min))

    def pop(self):
        if not self.s:
            return None
        else:
            return self.s.pop()[0]

    def top(self):
        if not self.s:
            return None
        return self.s[-1][0]

    def min(self):
        if not self.s:
            return None
        return self.s[-1][1]

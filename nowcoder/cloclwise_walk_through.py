# coding=utf-8
# 剑指offer 29 逆时针打印矩阵
# https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        self.left = 0
        self.right = len(matrix[0]) - 1
        self.top = 0
        self.bottom = len(matrix) - 1
        self.result =[]

        while self.top <= self.bottom and self.left<=self.right:
            if self.top <= self.bottom and self.left<=self.right:
                self.l2r(matrix)
            if self.top <= self.bottom and self.left<=self.right:
                self.t2b(matrix)
            if self.top <= self.bottom and self.left<=self.right:
                self.r2l(matrix)
            if self.top <= self.bottom and self.left<=self.right:
                self.b2t(matrix)
        return self.result
    def l2r(self, matrix):
        for i in range(self.left, self.right + 1):
            self.result.append( matrix[self.top][i])
        self.top += 1

    def t2b(self, matrix):
        for i in range(self.top, self.bottom + 1):
            self.result.append( matrix[i][self.right])
        self.right -= 1

    def r2l(self, matrix):
        for i in range(self.right, self.left - 1, -1):
            self.result.append( matrix[self.bottom][i])
        self.bottom -= 1

    def b2t(self, matrix):
        for i in range(self.bottom, self.top - 1, -1):
            self.result.append( matrix[i][self.left])
        self.left += 1


print Solution().printMatrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]

])
# print Solution().printMatrix([[1],[2],[3],[4],[5]])

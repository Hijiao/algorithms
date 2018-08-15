# coding=utf-8
# https://blog.csdn.net/na_beginning/article/details/62884939

# 01背包问题描述：有编号分别为a,b,c,d,e的五件物品，它们的重量分别是2,2,6,5,4，它们的价值分别是6,3,5,4,6，
# 每件物品数量只有一个，现在给你个承重为10的背包，如何让背包里装入的物品具有最大的价值总和？


class Solution:
    def get_max_values(self, weights, values, W):
        f = [{} for _ in weights]

        def calculate(i, w):
            if i < 0:
                return 0
            if w in f[i]:
                return f[i][w]

            if weights[i] > w:
                f[i][w] = 0
                return f[i][w]

            else:
                f[i][w] = max(calculate(i - 1, w), calculate(i - 1, w - weights[i]) + values[i])
                # print f
                return f[i][w]

        return calculate(len(weights) - 1, W)


# print Solution().get_max_values([2, 2, 6, 5, 4], [6, 3, 5, 4, 6], 10)


# 完全背包问题：

# 完全背包问题描述：有编号分别为a,b,c,d的四件物品，它们的重量分别是2,3,4,7，它们的价值分别是1,3,5,9，
# 每件物品数量无限个，现在给你个承重为10的背包，如何让背包里装入的物品具有最大的价值总和？

class Solution2:
    def get_max_value(self, weights, values, W):
        f = [{} for _ in range(len(weights))]

        def calculate(i, w):
            if i < 0:
                return 0
            if w in f[i]:
                return f[i][w]
            if weights[i] > w:
                f[i][w] = 0
                return f[i][w]
            else:
                f[i][w] = max(calculate(i - 1, w), calculate(i, w - weights[i]) + values[i])
                print f
                return f[i][w]

        # return max(calculate(len(weights) - 1, w + 1) for w in range(W))
        return calculate(3, 10)


print Solution2().get_max_value([2, 3, 4, 7], [1, 3, 5, 9], 10)

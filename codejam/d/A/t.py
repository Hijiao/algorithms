def gen(N, x1, x2, A, B, C, M, L):
    X = [0, x1, x2]
    ret = []

    # ret.append(x1+L)
    # ret.append(x2+L)

    for i in range(3, N + 1):
        X.append((A * X[i - 1] + B * X[i - 2] + C) % M)

    # for i in range(N):
    #     ret.append(X[i + 1] + L)
    X.pop(0)
    return X


print gen(6, 1, 1, 1, 1, 0, 100, 0)

print gen(10, 4, 3, 4, 1, 5, 20, -10)

print gen(10, 4, 3, 4, 1, 5, 20, -19)


class Solution:
    def cal(self, N, O, D, candis):
        # print candis
        pass


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, O, D = (int(s) for s in raw_input().split(" "))
    # print "-------------------", nums
    x1, x2, A, B, C, M, L = (int(s) for s in raw_input().split(" "))
    so = Solution()
    candis = gen(N, x1, x2, A, B, C, M, L)
    so.cal(N, O, D, candis)
    result = 0
    print "Case #{}: {}".format(i, result)

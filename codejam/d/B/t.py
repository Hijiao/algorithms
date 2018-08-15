def convert_2d(N, p, p2, A, B, C, M, h, h1, a, b, c, m):
    max_x = max(p, p2)

    ret = {}
    ret_0 = p
    ret_1 = p2

    het_0 = h
    het_1 = h1
    ret[ret_0] = het_0
    ret[ret_1] = het_1

    # max_g = max(p, p2)
    for i in range(2, N):
        ret_2 = (A * ret_1 + B * ret_0 + C) % M + 1
        het_2 = (a * het_1 + b * het_0 + c) % m + 1
        ret[ret_2] = het_2
        ret_1, ret_0 = ret_2, ret_1
        het_1, het_0 = het_2, het_1
        if max_x < ret_1:
            max_x = ret_1

    return max_x, ret


# def convert_2d(N, x, y):
#     ret = {}
#     max_x = 0
#     for i in range(N):
#         ret[x[i]] = y[i]
#         if x[i] > max_x:
#             max_x = x[i]
#     return max_x, ret


class Solution():
    def c1(self, p, x, max_p, max_x):
        # print "start cal max_p", max_p
        # print "max_P", max_p
        # print "p", p

        max_ranges = p[max_p] + max_p

        t_r = [0] * max_ranges
        t_l = [0] * max_ranges
        th = [0] * max_ranges

        # print "init"

        if 0 in p:
            t_r = p[0]

        for i in xrange(1, max_ranges):
            t_r[i] = max(t_r[i - 1] - 1, p.get(i, 0))

        # print "t_r"

        # print "t_r", t_r
        t_l[max_p] = p[max_p]

        for i in xrange(max_p, -1, -1):
            t_l[i] = max(t_l[i + 1] - 1, p.get(i, 0))
        # print "t_l"

        for i in range(max_ranges):
            th[i] = max(t_r[i], t_l[i])
        # print "t_l", t_l
        # print "th", th

        total = 0

        for bx in x:
            if x[bx] <= th[bx]:
                total += 1

        return total

    def c(self, ps, xs, max_p, max_x):
        # print "start cal max_p", max_p
        # print "max_P", max_p
        # print "p", p
        done = []
        total = 0

        def check(x, total):
            for p in ps:
                if ps[p] - xs[x] >= abs(p - x):
                    total += 1
                    return total
            return total

        for x in xs:
            total = check(x, total)

        return total


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n1, n2 = (int(s) for s in raw_input().split(" "))
    # print "-------------------", nums
    p, p2, A, B, C, M = (int(s) for s in raw_input().split(" "))

    # print " p, p2, A, B, C, M ", p, p2, A, B, C, M
    h, h1, a, b, c, m = (int(s) for s in raw_input().split(" "))
    # print "  h, h1, a, b, c, m", h, h1, a, b, c, m

    max_p, ps = convert_2d(n1, p, p2, A, B, C, M, h, h1, a, b, c, m)

    print "max_p, p ", max_p, ps
    p, p2, A, B, C, M = (int(s) for s in raw_input().split(" "))
    h, h1, a, b, c, m = (int(s) for s in raw_input().split(" "))

    max_x, xs = convert_2d(n2, p, p2, A, B, C, M, h, h1, a, b, c, m)
    print "max_p, p ", max_x, xs

    so = Solution()
    result = so.c(ps, xs, max_p, max_x)
    print "Case #{}: {}".format(i, result)

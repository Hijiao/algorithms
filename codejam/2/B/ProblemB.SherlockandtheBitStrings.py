def solve(kd, n, k, p):
    # print "kd, n, k, p",kd, n, k, p
    tail =  bin(p - 1)[2:]
    bp = '0' * (n - k-len(tail))+tail
    # print bp
    # print len(bp)
    pi = 0
    result = ''
    for i in range(1, n + 1):
        if kd.get(i) is None:
            result += bp[pi]
            pi += 1
        else:
            result += str(kd.get(i))
    return result


# print solve({2: '1'}, 3, 1, 2)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k, p = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    kd = {}

    for j in xrange(1, k + 1):
        a, b, c = [int(s) for s in raw_input().split(" ")]
        kd[a] = c
    result = solve(kd, n, k, p)

    print "Case #{}: {}".format(i, result)

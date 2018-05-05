def count(f, l):
    result = 2

    for i in xrange(f + 1, l):
        if '9' in str(i):
            continue
        elif sum([int(x) for x in str(i)]) % 9 != 0:
            result += 1
    return result

import sys
print sys.maxint
print 10**18
print count(211846857731552573 ,678637833737314507)
print "done"
# with open('A-small-attempt0.in') as input_file:
#     with open('result.txt', 'w') as output_file:
#         total = int(input_file.readline())
#         for i in range(total):
#             f, l = (input_file.readline()).strip().split(" ")
#             f, l = float(f), float(l)
#             r = count(f, l)
#             print "done :", i
#             output_file.write("Case #%s: %s\n" % (i + 1, r))
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i,count(n, m))

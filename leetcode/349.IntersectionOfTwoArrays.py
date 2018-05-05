class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) | set(nums2))


# print Solution().intersection([1, 2, 3], [2, 3, 4, 5])

result = []


def check(x, y, z):
    if x <= 1 and x+y <= 2:
        return True
    else:
        return False


for x in range(0, 4):
    for y in range(0, 4):
        z = 3 - x - y
        if z >= 0 and check(x, y, z):
            result.append((x, y, z))

print result
for x, y, z in result:
    print "(" + ")" * x + "(" + ")" * y + "(" + ")" * z

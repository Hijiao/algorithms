class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        R = len(matrix)
        if R == 0:
            return 0
        C = len(matrix[0])

        r = [[0 for i in range(C)] for j in range(R)]

        def find_longest(i, j):
            if r[i][j] != 0:
                return r[i][j]
            else:
                v = matrix[i][j]
                r[i][j] = 1 + max(
                    find_longest(i + 1, j) if i < R - 1 and v > matrix[i + 1][j] else 0,
                    find_longest(i - 1, j) if i > 0 and v > matrix[i - 1][j] else 0,
                    find_longest(i, j + 1) if j < C - 1 and v > matrix[i][j + 1] else 0,
                    find_longest(i, j - 1) if j > 0 and v > matrix[i][j - 1]else 0)
                return r[i][j]

        return max(find_longest(i, j) for i in range(R) for j in range(C))


# print Solution().longestIncreasingPath([[1,2]])

def p(i, j):
    print i, j
    return 0


#
# print max(p(i, j) for i in range(2) for j in range(3))

a = None
b = 1
print max(a - b if a is not None else None,None)

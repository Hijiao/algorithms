class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        if cols == 0:
            return 0
        visited = [[-1 for _ in range(cols)] for _ in range(rows)]

        def visit(pre, i, j):
            if pre <= matrix[i][j]:
                return 0

            if visited[i][j] != -1:
                return visited[i][j]
            else:
                step = max([
                    visit(matrix[i][j], i + 1, j) if i < rows - 1 else 0,
                    visit(matrix[i][j], i, j + 1) if j < cols - 1 else 0,
                    visit(matrix[i][j], i - 1, j) if i > 0 else 0,
                    visit(matrix[i][j], i, j - 1) if j > 0 else 0
                ]) + 1
                visited[i][j] = step
                return step

        #
        # for i in range(rows):
        #     for j in range(cols):
        #         visit(float('inf'), i, j)
        return max((visit(float("inf"), i, j) for i in range(rows) for j in range(cols)))


print Solution().longestIncreasingPath(
    [[9, 9, 4], [6, 6, 8], [2, 1, 1]])

r = [[]]

if r:
    print True
else:
    print False

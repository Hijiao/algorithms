class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [0 for _ in range(numCourses)]
        out_degree = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            out_degree[a].append(b)
            in_degree[b] += 1

        queue = [i for i in range(numCourses) if in_degree[i] == 0]

        k = 0
        while queue:
            k += 1
            q = queue.pop(0)
            for b in out_degree[q]:
                in_degree[b] -= 1
                if in_degree[b] == 0:
                    queue.append(b)

        return k == numCourses


print Solution().canFinish(2, [[1, 0], [0, 1]])

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
        in_degree = [0] * numCourses
        out_degree = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            in_degree[prerequisite[1]] += 1
            out_degree[prerequisite[0]].append(prerequisite[1])
        queue = [index for index in range(numCourses) if in_degree[index] == 0]
        result = []
        out_count = 0
        while queue:
            q = queue.pop(0)
            out_count += 1
            result.insert(0, q)
            for item in out_degree[q]:
                in_degree[item] -= 1
                if in_degree[item] == 0:
                    queue.append(item)
        if out_count == numCourses:
            return result
        else:
            return []
    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        postCourse = [[]for i in xrange(numCourses)]
        indegree = [0] * numCourses
        for p in prerequisites:
            postCourse[p[1]].append(p[0])
            indegree[p[0]] += 1
        queue = []
        res = []
        for i in xrange(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop(0)
            res.append(course)
            for nb in postCourse[course]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    queue.append(nb)
        return [] if len(res) < numCourses else res

print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])

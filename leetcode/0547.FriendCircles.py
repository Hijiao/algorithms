class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return 0
        R = len(M)
        C = len(M[0])
        path_map = [[0 for i in range(C)] for j in range(R)]
        counter = 0

        def check(i):
            for j in range(R):
                if path_map[i][j] == 0:
                    path_map[i][j] = 1
                    path_map[j][i] = 1
                else:
                    continue
                if M[i][j] == 1:
                    check(j)

        for i in range(R):
            for j in range(i, C):
                if path_map[i][j] == 0:
                    check(i)
                    counter += 1
        return counter
print Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
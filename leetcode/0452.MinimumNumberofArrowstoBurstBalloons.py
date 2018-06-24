from collections import defaultdict
class Solution(object):

    def __init__(self):
        self.d =defaultdict(list)
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        x = float('-inf')
        count =0
        for index,p in enumerate(points):
            if p[0] <= x:
                continue
            else:
                x =p[1]
                count+=1
        return count

print Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
from heapq import *


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        d = {}
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1
        h = []
        for key in d:
            heappush(h, -d[key])

        finished = 0
        count = 0
        while True:
            temp = []
            for i in range(n):
                count += 1
                if len(h) >= 1:
                    task = heappop(h)
                    finished += 1
                    if finished == len(tasks):
                        return count
                    if task < -1:
                        temp.append(task + 1)

            for t in temp:
                heappush(h, t)

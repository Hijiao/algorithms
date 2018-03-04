class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        step = [0, 0]
        for i in range(2, len(cost) + 1, 1):
            step.append(min(step[i - 1] + cost[i - 1], step[i - 2] + cost[i - 2]))
        return step[-1]


if __name__ == '__main__':
    cost = [1, 1, 0, 0]
    print Solution().minCostClimbingStairs(cost)

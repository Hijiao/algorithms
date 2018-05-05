class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        i = 0
        count = 0
        while True:
            if i >= len(coins):
                break
            if amount - coins[i] < 0:
                i += 1
            elif amount - coins[i] > 0:
                count += 1
                amount -= coins[i]
            else:
                count += 1
                amount -= coins[i]
                break
        if amount == 0:
            return count
        else:
            return -1


print Solution().coinChange([186,419,83,408],6249)
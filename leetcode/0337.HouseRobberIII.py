# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level_sum=[]
        queue = [root]
        while queue:
            level_sum.append(sum(x.val for x in queue))
            queue = filter(None,[node for q in queue for node in [q.right,q.left]])
        print level_sum
        return self.rob1(level_sum)


    def rob1(self,nums):
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]
        if len(nums) ==2:
            return max(nums)
        dp=[0]* len(nums)
        dp[0] = nums[0]
        dp[1] =max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        print dp
        return dp[-1]

root= TreeNode(2)
root.left = TreeNode(1)

root.left.right = TreeNode(4)

root.right= TreeNode(3)
# root.right.right=TreeNode(1)


print Solution().rob(root)
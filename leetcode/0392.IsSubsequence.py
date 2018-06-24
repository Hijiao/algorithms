class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if not s and not t:
        #     return True
        # if not s:
        #     return True
        # if not t:
        #     return False
        #
        #
        # si = 0
        # for ti in range(len(t)):
        #     if t[ti] == s[si]:
        #         si+=1
        #     if si ==len(s):
        #         return True
        # return False
        if len(s) >len(t):
            return  False
        start=0
        for item in s:
            index = t.find(item,start)
            if index ==-1:
                return False
            start= index+1
        return True
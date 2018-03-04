#https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
        	return ""
        prefix=strs[0]
        for s in strs:
        	while(not s.startswith(prefix)):
        		if len(prefix) == 1:
        			return ""
        		prefix=prefix[:-1]
        return prefix
        
        
if __name__ == "__main__":
	Solution().longestCommonPrefix([])
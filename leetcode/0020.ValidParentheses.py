class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:
            if i == "}":
                if len(l) == 0 or l[-1] != "{":
                    return False
                l.pop()
            elif i == "]":
                if len(l) == 0 or l[-1] != "[":
                    return False
                l.pop()
            elif i == ")":
                if len(l) == 0 or l[-1] != "(":
                    return False
                l.pop()
            else:
                l.append(i)
        if len(l) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isValid("()"))

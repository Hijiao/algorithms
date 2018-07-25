# https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

def co(a, b):
    la = len(str(a))
    lb = len(str(b))
    # return a * (10 ** (lb)) + b - (b * (10 ** (la)) + a)
    return int(str(a)+str(b)) -int(str(b)+str(a))

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        t = sorted(numbers, cmp=co)
        return "".join(map(str, t))


print Solution().PrintMinNumber([321,32,3])
class Solution(object):
    def __init__(self):
        self.ret = []

    def convert(self, start_ip, n, count):
        if count <= 0:
            return
        next_step = 2 ** (32 - n)
        next_n = n
        while next_step > count:
            next_n += 1
            next_step = 2 ** (32 - next_n)

        self.ret.append((start_ip + next_step, next_n))
        self.convert(start_ip + next_step, next_n, count - next_step)

    def conver_str_2_int(self, s):
        ret = 0
        ss = s.split('.')
        for i in range(4):
            ret += int(ss[i]) << (3 - i) * 8
        return ret

    def input(self, ip, count):
        int_ip = self.conver_str_2_int(ip)
        bin_ip = bin(int_ip)[1:]
        n = 0
        for i in range(31, -1, -1):
            if bin_ip[i] != "0":
                n = i + 1
                break
        self.ret.append((int_ip, n))
        self.convert(int_ip, n, count - 2 ** (32 - n))

        print self.ret


r = Solution().input("127.0.0.2", 9)
print(r)

class Solution(object):
    def __init__(self):
        self.dict ={}

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.shopping(price, special, needs)

    def shopping(self, price, special, needs):
        needs =tuple(needs)
        if self.dict.get(needs):
            return self.dict[needs]

        ret = sum(price[i] * needs[i] for i in range(len(needs)))

        for s in special:
            new_needs = []
            for i in range(len(needs)):
                if needs[i] - s[i] < 0:
                    continue
                else:
                    new_needs.append(needs[i] - s[i])
            if len(new_needs) == len(needs):
                ret = min(ret, s[len(needs)] + self.shopping(price, special, new_needs))
        self.dict[needs] =ret
        return ret


# print Solution().shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1])

d={}
while True:
    i = raw_input()
    if i in d:
        print d[i]
    else:
        d[i] = 1
    print d

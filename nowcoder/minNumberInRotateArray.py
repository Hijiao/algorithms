# -*- coding:utf-8 -*-
#[编程题]旋转数组的最小数字

#https://www.nowcoder.com/questionTerminal/9f3231a991af4f55b95579b44b7a01ba

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) < 3:
            return min(rotateArray)
        base = len(rotateArray) / 2
        if base == 0:
            return min(rotateArray)
        if rotateArray[base - 1] > rotateArray[base]:
            return rotateArray[base]
        if rotateArray[base] > rotateArray[base + 1]:
            return rotateArray[base + 1]
        if rotateArray[len(rotateArray)-1] < rotateArray[base]:
            return self.minNumberInRotateArray(rotateArray[base + 1:])
        else:
            return self.minNumberInRotateArray(rotateArray[:base])




print Solution().minNumberInRotateArray(
[6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335])
import bisect


class MyCalendar(object):
    def __init__(self):
        self.array = [(float('-inf'), float('-inf')), (float('inf'), float('inf'))]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        index = find_index(self.array,end)
        if self.array[index - 1][1] <= start and self.array[index][0] >= end:
            self.array.insert(index, (start, end))
            return True
        else:
            return False


def find_index(array, value):
    low = 0
    height = len(array)

    while low < height:
        index = (low + height) // 2

        if array[index][0] > value:
            height = index
        else:
            low = index + 1
    return low




def t(self):
    bisect.bisect_left()



    # Your MyCalendar object will be instantiated and called as such:
    # obj = MyCalendar()
    # param_1 = obj.book(start,end)


m = MyCalendar()
print m.book(37, 50)
print m.book(4, 17)
print m.book(35, 48)

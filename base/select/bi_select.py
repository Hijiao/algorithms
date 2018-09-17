from bisect import bisect

def bisect(array, val):
    low = 0
    height = len(array)

    while low < height:
        base = (low + height) // 2

        if array[base] > val:
            height = base
        else:
            low = base + 1

    return low


print(bisect([0, 1, 2, 3], 2))

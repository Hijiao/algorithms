def quicksort(l, start, end):
    if start < end:
        i, j = start, end
        base = l[i]
        while i < j:
            while (i < j) and l[j] >= base:
                j -= 1
            l[i] = l[j]
            while (i < j) and l[i] <= base:
                i += 1
            l[j] = l[i]
        l[i] = base
        quicksort(l, start, i-1)
        quicksort(l, i+1, end)
    return l


myList = [49, 38, 65, 97, 76, 13, 27, 49]
print("Quick Sort: ")
quicksort(myList, 0, len(myList) - 1)
print(myList)

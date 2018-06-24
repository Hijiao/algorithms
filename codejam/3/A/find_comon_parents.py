a = [1, 2,24]
b = [1, 4,6,8]


def find_common_parent(a, b):
    path = []
    i = 0
    while i < len(a) and i < len(b):
        if a[i] == b[i]:
            if path:
                path.pop()
            if path:
                path.pop()

        path.append(a[i])
        path.append(b[i])
        i+=1

    if i < len(a):
        path += a[i:]
    else:
        path += b[i:]

    return path


print find_common_parent(a, b)

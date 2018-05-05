raw = int(raw_input())
col = int(raw_input())

m = []
for i in range(raw):
    m.append([int(x) for x in raw_input().split(" ")])

print m


def count(i, j, direction):
    if i >= raw or i < 0:
        return 0
    if j >= col or j < 0:
        return 0
    if m[i][j] == 0:
        return 0
    else:
        if direction == "left":

            return 1 + count(i, j - 1, direction)
        elif direction == 'right':
            return 1 + count(i, j + 1, direction)
        elif direction == "up":
            return 1 + count(i - 1, j, direction)
        else:
            return 1 + count(i + 1, j, direction)


r = {}


def find():
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                c = sum([count(i, j, "left"), count(i, j, "right"), count(i, j, "up"), count(i, j, "lower")])
                if c in r:
                    r[c].append((i, j))
                else:
                    r[c] = [(i, j)]


find()

max_count = max(r.keys())
for item in r[max_count]:
    print item[0], item[1]

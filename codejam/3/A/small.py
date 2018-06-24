import sys

sys.setrecursionlimit(1000000)
class Solution():
    def __init__(self):
        self.found = False
        self.ring = []
        self.visited_path_dict = {}
        self.distance_dict = {}
        self.less_pairs_dict = {}
        self.full_map = {}

    def salve(self, a, b):
        if a < b:
            if a in self.less_pairs_dict:

                self.less_pairs_dict[a].append(b)
            else:
                self.less_pairs_dict[a] = [b]
        else:
            if b in self.less_pairs_dict:
                self.less_pairs_dict[b].append(a)
            else:
                self.less_pairs_dict[b] = [a]

        if a in self.full_map:

            self.full_map.get(a).append(b)
        else:
            self.full_map[a] = [b]

        if b in self.full_map:
            self.full_map[b].append(a)
        else:
            self.full_map[b] = [a]

    def find_ring(self, pairs_dict, nums):
        path = []

        def dfs(n):
            if self.found:
                return
            pairs = pairs_dict.get(n, [])
            path.append(n)

            for pair in pairs:
                dst = pair
                if dst in self.visited_path_dict:
                    # self.ring = self.visited_path_dict[dst][path.index(n):]
                    self.ring = find_common_parent(path, self.visited_path_dict[dst])
                    self.found = True
                    return
                else:
                    self.visited_path_dict[dst] = path[:] + [dst]
                    dfs(dst)
            path.pop()

        dfs(1)

        dist = 0
        queue = self.ring[:]
        for n in self.ring:
            self.distance_dict[n] = 0
            for node in self.full_map.get(n, []):
                if node not in queue:
                    queue.append(node)
        for n in self.ring:
            queue.pop(0)

        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node in self.distance_dict:
                    continue
                else:
                    self.distance_dict[node] = dist + 1
                    ner = self.full_map.get(node, [])
                    for ne in ner:
                        if ne not in self.distance_dict:
                            queue.append(ne)
            dist += 1
        # print self.distance_dict
        return [str(self.distance_dict[i]) for i in range(1, nums + 1)]
        # for node in self.ring:
        #     self.distance_dict[node] = 0
        #
        # for i in range(1, 6):
        #     self.find(i, pairs_dict)


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

    return list(set(path))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    nums = int(raw_input())
    # print "-------------------", nums
    so = Solution()
    for num in range(nums):
        a, b = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        so.salve(a, b)
    result = " ".join(so.find_ring(so.less_pairs_dict, nums))
    print "Case #{}: {}".format(i, result)

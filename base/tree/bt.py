class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, value, node):
        if node is None:
            node = Node(value)
        elif value < node.value:
            node.left = self.insert(value, node.left)
        elif value > node.value:
            node.right = self.insert(value, node.right)
        else:
            pass
        return node

    def pre_order(self, node):
        if node is None:
            pass
        else:
            print node.value
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            pass
        else:
            self.in_order(node.left)
            print node.value
            self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            pass
        else:
            self.post_order(node.left)
            self.post_order(node.right)
            print node.value


if __name__ == '__main__':
    t = Tree()
    for i in [3, 1, 2, 4, 8, 0]:
        t.root = t.insert(i, t.root)
        # print "root", t.root.value
    t.pre_order(t.root)
    print "-----"
    t.in_order(t.root)

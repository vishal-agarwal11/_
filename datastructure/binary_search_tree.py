class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def traverse_print(self):
        if self.root:
            self._traverse_print(self.root)

    def _traverse_print(self, curr):
        if curr.left and curr.right:
            self._traverse_print(curr.left)
            print(curr.data)
            self._traverse_print(curr.right)
        elif not curr.left and curr.right:
            print(curr.data)
            self._traverse_print(curr.right)
        elif not curr.right and curr.left:
            self._traverse_print(curr.left)
            print(curr.data)
        elif not curr.left and not curr.right:
            print(curr.data)

    def _traverse_insert(self, ptr, data):
        if data <= ptr.data and ptr.left:
            self._traverse_insert(ptr.left, data)
        elif data <= ptr.data and not ptr.left:
            ptr.left = Node(data)
        elif data > ptr.data and ptr.right:
            self._traverse_insert(ptr.right, data)
        elif data > ptr.data and not ptr.right:
            ptr.right = Node(data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._traverse_insert(self.root, data)


if __name__ == "__main__":
    t = Tree()
    t.insert(21)
    t.insert(25)
    t.insert(28)
    t.insert(29)
    t.insert(223)
    t.insert(26)
    t.insert(23)
    t.insert(15)
    t.insert(18)
    t.insert(9)
    t.insert(6)
    t.traverse_print()

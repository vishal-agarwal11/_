class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def terminal(self, this_node):
        while(this_node.next):
            this_node = this_node.next
        return this_node

    def insert(self, data):
        print(f"Inserting {data}")
        if not self.head:
            self.head = Node(data)
        else:
            last_node = self.terminal(self.head)
            last_node.next = Node(data)

    def traverse(self, this_node):
        print(this_node.info, end="|")
        if this_node.next:
            self.traverse(this_node.next)


if __name__ == "__main__":
    linklist = LinkedList()
    linklist.insert(3)
    linklist.insert(4)
    linklist.insert(5)
    linklist.insert(7)
    linklist.insert(9)
    print("\n")
    linklist.traverse(linklist.head)
    print("\n")

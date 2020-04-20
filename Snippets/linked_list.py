import sys
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
        if not self.head:
            self.head = Node(data)
        else:
            last_node = self.terminal(self.head)
            last_node.next = Node(data)

    def traverse(self, this_node):
        if not self.head:
            print("Link list is empty")
            return
        print(this_node.info, end="|")
        if this_node.next:
            self.traverse(this_node.next)


if __name__ == "__main__":

    print(f"i - Insert a node")
    print(f"p - Print link list")
    print(f"q - quit")
    linklist = LinkedList()
    input_ = input("Enter Option:")
    while(input_ != "q"):
        if input_ == "i":
            print("##You have chosen to Insert in the link list##")
            item = input("Enter element:")
            print(f"Inserting {item}")
            linklist.insert(item)
        elif input_ == "p":
            print("You have chosen to Print the link list")
            print("\n")
            linklist.traverse(linklist.head)
            print("\n")
        elif input_ == "q":
            print("Quitting")
            sys.exit(0)
        else:
            print("Invalid Input")
        input_ = input("Enter Option:")


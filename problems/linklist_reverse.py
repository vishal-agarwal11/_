class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, val):
        print(f"Inserting {val}")
        if self.root is None:
            self.root = Node(val)
        else:
            last_node = self.traverselast(self.root)
            last_node.next = Node(val)

    def traverselast(self, this_node, print_node=False):
        while this_node.next:
            if print_node:
                print(this_node.val)
            this_node = this_node.next
        if print_node:
            print(this_node.val)
        return this_node


    def reverse(self):
        prev = None
        current = self.root
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.root = prev 



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(3)
    ll.insert(13)
    ll.insert(31)
    ll.insert(17)
    ll.insert(8)
    ll.insert(4)
    ll.insert(2)
    ll.insert(23)

    #ll.traverselast(ll.root, print_node=True)

    ll.reverse()
    ll.traverselast(ll.root, print_node=True)


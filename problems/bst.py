class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, info):
        if not self.root:
            # print(f"Inserting {info} at root!")
            self.root = Node(info)
        else:
            self.ti(self.root, info)

    def ti(self, this_node, info):
        if info <= this_node.info and this_node.left:
            self.ti(this_node.left, info)
        elif info <= this_node.info and not this_node.left:
            # print(f"Inserting {info} in left of {this_node.info}")
            this_node.left = Node(info)
        elif info > this_node.info and this_node.right:
            self.ti(this_node.right, info)
        elif info > this_node.info and not this_node.right:
            # print(f"Inserting {info} in right of {this_node.info}")
            this_node.right = Node(info)

    def traverse(self, **kwargs):
        this_node = kwargs.get("this_node", self.root)
        if this_node.left and this_node.right:
            self.traverse(this_node=this_node.left)
            # print(this_node.info)
            self.traverse(this_node=this_node.right)
        elif this_node.left and not this_node.right:
            self.traverse(this_node=this_node.left)
            # print(this_node.info)
        elif not this_node.left and this_node.right:
            # print(this_node.info)
            self.traverse(this_node=this_node.right)
        elif not this_node.left and not this_node.right:
            pass
            # print(this_node.info)

    def checkBST(self, root_node):
        if root_node.left and root_node.right:
            if not root_node.left.info <= root_node.info:
                return False
            else:
                # print(f"{root_node.left.info} <= {root_node.info}")
                self.checkBST(root_node.left)

            if not root_node.right.info > root_node.info:
                return False
            else:
                # print(f"{root_node.right.info} > {root_node.info}")
                self.checkBST(root_node.right)

        elif root_node.left and not root_node.right:
            if not root_node.left.info <= root_node.info:
                return False
            else:
                # print(f"{root_node.left.info} <= {root_node.info}")
                self.checkBST(root_node.left)
        elif not root_node.left and root_node.right:
            if not root_node.right.info > root_node.info:
                return False
            else:
                # print(f"{root_node.right.info} > {root_node.info}")
                self.checkBST(root_node.right)
        return True

    def height(self, root_node):
        if not root_node:
            return 0
        # try:
        #     print(f"Calling height({root_node.left.info})")
        # except:pass
        left_height = self.height(root_node.left)
        # try:
        #     print(f"Calling height({root_node.right.info})")
        # except:pass
        right_height = self.height(root_node.right)
        if left_height > right_height:
            h = 1 + left_height
        else:
            h = 1 + right_height
        # print(f"h={h}")
        return h

    def level_traversing(self, queue=[]):
        #print(f"{queue}")
        if len(queue) != 0:
            try:
                queue.append(queue[0].left)
            except:pass

            try:
                queue.append(queue[0].right)
            except:pass
            if len(queue) > 1 and not queue[0]:
                queue.pop(0)
                self.level_traversing()
            elif len(queue) > 1 and queue[0]:
                print(queue[0].info)
                queue.pop(0)
                self.level_traversing()
        elif len(queue) == 0:
            queue.append(self.root)
            self.level_traversing()



if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(11)
    bst.insert(15)
    bst.insert(9)
    bst.insert(8)
    bst.insert(18)
    bst.insert(21)
    bst.insert(40)
    bst.insert(3)
    bst.traverse()

    # print(bst.checkBST(bst.root))
    # print(bst.height(bst.root))
    bst.level_traversing()

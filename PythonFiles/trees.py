# implementation of binary search tree
# where all left nodes are smaller than root
# and all right nodes are greater than root


class BinarySearchTreeNode:
    def __init__(self, data, left=None, right=None):
        # data for root node
        self.data = data
        # left child
        self.left = left
        # right child
        self.right = right

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def pre_order_traversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.pre_order_traversal(root.get_left())
            result = result + self.pre_order_traversal(root.get_right())

        return result

    def in_order_traversal(self, root):
        result = []
        if root:
            result = self.in_order_traversal(root.get_left())
            result.append(root.data)
            result = result + self.in_order_traversal(root.get_right())

        return result

    def post_order_traversal(self, root):
        result = []
        if root:
            result = self.post_order_traversal(root.get_left())
            result = result + self.post_order_traversal(root.get_right())
            result.append(root.data)

        return result


root = BinarySearchTreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)


print(root.pre_order_traversal(root))
print(root.in_order_traversal(root))
print(root.post_order_traversal(root))

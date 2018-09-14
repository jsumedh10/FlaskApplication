class BinaryTreeNode:
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


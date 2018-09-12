"""
This file implements stacks using singly linked lists.
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def has_next(self):
        return self.next is not None


class Stack(object):

    def __init__(self, data):
        self.data = data
        self.head = None
        if data:
            for value in data:
                self.push(value)

    # push data given from the input list
    def push(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def print_stack(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()


lst = [1,2,3,4,5]
my_stack = Stack(lst)
print(my_stack.pop()+1)
# my_stack.push(6)
# my_stack.print_stack()
# my_stack.push(7)
# my_stack.print_stack()
# my_stack.pop()
# my_stack.print_stack()

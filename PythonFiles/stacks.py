"""
This file implements stacks using singly linked lists.
"""

from LinkedLists import Node


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

# Singly linked lists implementation


# create a NODE class
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


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

        self.length += 1

    def insert_at_position(self, data, position):
        if 0 > position or self.length < position:
            return None
        else:
            if position == 0:
                self.insert_at_beginning(data)
            elif position == self.length:
                self.insert_at_end(data)
            else:
                new_node = Node(data)
                current = self.head
                count = 1
                while count <= (position - 2):
                    count += 1
                    current = current.get_next()

                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length += 1

    def list_length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count

    def print_list(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()


my_list = LinkedList()
my_list.insert_at_position('A',0)
my_list.insert_at_position('B',1)
my_list.insert_at_position('D',2)
my_list.insert_at_position('E',3)
my_list.insert_at_position('C',3)
# my_list.insert_at_end(3)
# my_list.insert_at_beginning(5)
# my_list.insert_at_end(10)
# my_list.insert_at_end(15)
# my_list.insert_at_beginning(20)
# # my_list.insert_at_beginning(100)
# # my_list.insert_at_end(500)
# # print(my_list.list_length())
my_list.print_list()
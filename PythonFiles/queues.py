class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class Queue:

    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.front = self.rear = new_node
        else:
            self.rear.set_next(new_node)
        self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty. Can't perform Dequeue.")
        else:
            val = self.front.get_data()

        self.front = self.front.get_next()
        self.size -= 1

        return val

    def is_empty(self):
        return self.size == 0

    def get_front(self):
        return self.front.get_data()

    def get_rear(self):
        return self.rear.get_data()

    def get_size(self):
        return self.size

    def print_queue(self):
        if self.size == 0:
            # print("Queue is empty.")
            raise Exception("Queue is empty")
        lst = []
        current = self.front
        while current:
            lst.append(current.get_data())
            current = current.get_next()

        return lst


q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.print_queue())
print(q.dequeue())
print(q.print_queue())
print(q.get_front())
print(q.get_rear())
print(q.is_empty())
# print(q.get_front())
# print(q.get_rear())
# print(q.get_size())


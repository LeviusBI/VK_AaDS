class Node():
    def __init__(self, data=None, fut=None):
        self.data = data
        self.prev = None
        self.next = fut




class LinkedList():
    """
    Реализация односвязного списка на питончике
    """
    def __init__(self, head=None):
        if type(head) == '__main__.Node':
            self.head = head
        else:
            self.head = Node(head)
        self.size = 0

        if head != None:
            self.size = 1

    def add_new_head(self, data):
        """
        Добавление элемента в начало списка
        """
        
        node = Node(n)

        if self.head is None:
            self.head = node
            self.size += 1

        
        noda.next = self.head
        self.size += 1
        self.head = noda

    def append(self, n):
        """
        Добавление элемента в конец списка
        """
        node = Node(n)
        if self.head is None:
            self.head = node
            self.size += 1
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node


    def print_list(self):

        current_node = self.head

        to_print = ""

        while current_node is not None:
            to_print += str(current_node.data)

            if current_node.next:
                to_print += " -> "
            current_node = current_node.next

        print(to_print)

    def insert(self, after, n):
        to_find = self.head
        while to_find is not None:
            if to_find.data == after:
                break
            to_find = to_find.next

        if to_find is not None:
            node = Node(n)
            node.next = to_find.next
            to_find.next = node

class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        if self.top:
            self.top = new_node
            return

        new_node.next = self.top

        self.top = new_node

    def pop(self):

        if not self.top:
            return -1

        top = self.top

        if self.top.next is not None:
            self.top = self.top.next
        else:
            self.top = None
        return top.data


class Queue(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
        
    def pop(self):
        if self.head.next == self.tail:
            return None
        pop_result = self.tail.prev

        self.tail.prev = pop_result.prev

        pop_result.prev.next = pop_result.next

        pop_result.next = None
        pop_result.prev = None

        self.size -= 1
        return pop_result.data
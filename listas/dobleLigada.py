class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ListaDoblemeteLigada:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete(self, data):
        if self.head is None:
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def show(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

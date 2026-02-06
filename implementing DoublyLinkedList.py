class Node:
    def __init__(self,value,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev = prev
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_beginning(self,value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node = Node(value)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
    def add_end(self,value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node
    def print_forward(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            current = self.head
            while current is not None:
                print(f"{current.value} <--> ", end="")
                current = current.next
            print("None")
    def print_backward(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            current = self.tail
            while current is not None:
                print(f"{current.value} <--> ", end="")
                current = current.prev
            print("None")

    def delete(self,value):
        if self.head is None:
            print("Can't delete from an empty list")
            return
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    if  self.head == self.tail:
                        self.head = None
                        self.tail = None
                        print("The list is empty")
                        return
                    elif current == self.head:
                        self.head = self.head.next
                        self.head.prev = None
                        return
                    elif current == self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = None
                        return
                    else:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                    return
                else:
                    current = current.next

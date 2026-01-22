class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
     # Method to add values at the beginning of the list
    def add_beginning(self,value):
        new_node = Node(value,self.head)
        self.head = new_node
    # Method to print the list
    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.value}-> ",end="")
            current = current.next
        print("None")
    # Method to add values at the end of the list
    def add_end(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
    # Method to delete a value at the end ,middle or beginning of the list
    def delete(self,value):
        if self.head is None:
            print("You can't delete because the List is empty")
        if self.head.value == value:
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                else:
                    current = current.next
    # Method to search for a value in the end , middle ,or beginning of the list
    def search(self,value):
        if self.head is None:
            print("You can't search because the List is empty")
            return
        if self.head.value == value:
            print("Value is in the list")
            return
        else:
            current = self.head
            while current.next is not None:
                if current.value == value:
                    print("Value is in the list")
                    return
                else:
                    current = current.next
            print("Value is not in the list")


llist = LinkedList()
llist.add_beginning(5)
llist.add_beginning(4)
llist.add_end(6)
llist.add_end(8)
llist.search(6)
llist.search(10)
llist.delete(5)

llist.print_list()


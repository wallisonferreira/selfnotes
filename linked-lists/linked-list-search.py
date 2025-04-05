class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
        
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
            
    def search(self, item):
        if self.head is not None:
            node = self.head
            while node is not None:
                if node.data == item:
                    print("Found it!")
                    return True
                else:
                    node = node.next
            print("Not found")
            return False
                    
        
# linked_list = LinkedList()
# linked_list.append_node("Wallison")
# linked_list.append_node("Santos")
# linked_list.append_node("Ferreira")
# linked_list.print_list()

linked_list = LinkedList()
linked_list.append_node(4)
linked_list.append_node(5)
linked_list.append_node(6)
linked_list.append_node(8)
linked_list.search(7)


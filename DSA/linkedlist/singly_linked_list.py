class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
class Singlylinkedlist():
    def __init__(self):
        self.head = None
    def append(self,val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            curr = self.head
            while curr.next !=None:
                curr = curr.next
            curr.next = newnode
    def traversal(self):
        if self.head == None:
            print('Singly Linked list is empty')
        else:
            curr = self.head
            while curr !=None:
                print(curr.val, end='->')
                curr = curr.next
            print()
sll = Singlylinkedlist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(1)
sll.traversal() 
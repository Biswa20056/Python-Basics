class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class Singlylinkedlist:
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
    def insert_at(self,val,position):
        newnode = Node(val)
        if position==0:
            newnode.next = self.head
            self.head = newnode
        else:
            current = self.head
            prev = None
            count = 0
            while current is not None and count < position:
                prev = current
                current = current.next
                count +=1
            prev.next = newnode
            newnode.next = current
    def delete(self,val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return 
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return 
                else:
                    print('Node not found')

    def traverse(self):
        if self.head==None:
            print('linked list is empty')
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end='->')
                curr = curr.next
            print()
sll = Singlylinkedlist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.insert_at(50,2)
sll.delete(60)
sll.traverse()


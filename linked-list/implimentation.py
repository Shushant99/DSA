class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    
    #insertion at end
    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
#insert at begning
    def prepend(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    #deleting first occurence of a value
    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next

    #searching in linked list
    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
    def display(self):
        elements=[]
        


l=linkedlist()
l.append(5)
l.append(50)
l.append(55)
print(l.search(0))
print(l.head.next.next.data)
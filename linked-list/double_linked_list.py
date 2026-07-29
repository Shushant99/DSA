class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class double_linked_list:
    def __init__(self):
        self.head=None
    
    #insert at begning 
    def prepend(self,val):
        new_node=Node(val)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head=new_node

    #insert at end
    def append(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    

    #printing a D-linkedlist
    def printLL(self):
        temp=self.head
        while temp:
            print( temp.data , end="<->")
            temp=temp.next
        print("None")




s=double_linked_list()
s.append(5)
s.append(8)
s.prepend(3)
s.printLL()




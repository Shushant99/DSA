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
    

    #searching in linked list
    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
    # print linked list
    def display(self):
        elements=[]
        current=self.head
        while current:
            elements.append(str(current.data))
            current=current.next

        print("->".join(elements)+"->None")
    # reverse a linked list
    def reverselist(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    # printing a linked list nodes
    def printlink(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    #find length of linked list
    def lengthlink(self):
        current=self.head
        length=0
        while current:
            length+=1
            current=current.next
        return length
    #access node  at index k
    def accesslinkedk(self,index):
        self.index=index
        counter=0
        current=self.head
        while counter!=index:
            current=current.next
            counter+=1
        return current.data

    #insert after a given node
    def insertlinkedNode(self,index,data):
        new_node=node(data)
        if index==1:
            new_node.next=self.head
            self.head=new_node
            return
        
        count=1
        current=self.head
        while current is not None and count<index-1:
            current=current.next
            count+=1
        if current is None:
            print("index out of range")
            return
        new_node.next=current.next
        current.next=new_node
        

        
    #insert at pos k
    def insertlinked(self, index,data):
        new_node=node(data)
        if index==1:
            new_node.next=self.head
            self.head=new_node
            return
        
        count=1
        current=self.head
        while current is not None and count<index-1:
            current=current.next
            count+=1
        if current is None:
            print("index out of range")
            return
        new_node.next=current.next
        current.next=new_node
    
    #delete head
    def delhead(self):
        if self.head is None:
            print("no nodes present")
            return 
        temp=self.head
        self.head=self.head.next
        temp.next=None
    #del tail of a linked list
    def deltail(self):
        curr=self.head
        if curr is None:
            print("no node present")
            return
        if curr.next is None:
            self.head=None
            return
        while curr.next.next is not None:
            curr=curr.next
        curr.next=None
    #delete node by value
    def delval(self,val):
        curr=self.head
        if curr and curr.data==val:
            self.head=curr.next
            return
        while curr and curr.next:
            if curr.next.data==val:
                curr.next=curr.next.next
                return
            curr=curr.next
        
    #delete node at pos k with 0 indexed linked list
    def delpos(self,pos):
        curr=self.head
        

        


l=linkedlist()
for i in range(10):
    l.append(i)
l.delval(4)
l.display()

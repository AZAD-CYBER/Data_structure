class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head 

        self.head=new_node
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("\n")

    def delete_node(self,pos):
        temp=self.head
        pre=None
        size=self.calcSize()
        if pos<1 or pos>size:
            print("enter valid one")
            return
        if pos==1:
            self.head=temp.next
            print("value",temp.data)
            return 
        for i in range(0,pos-1):
            pre=temp
            temp=temp.next
            
            # pos-=1
        pre.next = temp.next 
        print ("Value deleted: ", temp.data) 
        


    def calcSize (self):
        size = 0 
        node = self.head 
	  
        while node is not None:
            node = node.next 
            size += 1 

        return size 
    
#Drive Code
ll = LinkedList () 
	    
ll.insert (12) 
ll.insert (16) 
ll.insert (20) 
ll.insert (24) 
ll.insert (30) 
ll.insert (22) 
ll.display()

ll.delete_node (1) 
ll.display () 
	    
ll.delete_node (3) 
ll.display () 
	    
# ll.delete_node (4) 
# ll.display () 
	    
# ll.delete_node (-2) 
# ll.delete_node (10) 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    
    def pop(self):
        if self.isempty():
            return None
        else:
            pop_node=self.head
            self.head=self.head.next
            pop_node.next=None
            return "Pop element..",pop_node.data
    
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        iter_node=self.head
        if self.isempty():
            print("No element")
        else:
            while iter_node:
                print(iter_node.data,end="")
                iter_node=iter_node.next
                if(iter_node!=None):
                    print("->",end="")
            return 


if __name__=="__main__":
    MyStack=Stack()

    MyStack.push(1)
    MyStack.push(2)
    MyStack.push(3)
    MyStack.push(4)
    MyStack.push(5)

    MyStack.display()

    print("\nTop element is ",MyStack.peek())

    print(MyStack.pop())
    print(MyStack.pop())

    MyStack.display()

    print("\nTop element is ",MyStack.peek())
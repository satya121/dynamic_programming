    #LINKED LIST
'''
    The first node is called 'Head' : initially none
    The last node is called 'Tail' : initially none
    The linked list is displayes using the variable 'temp' (temporary variable)
    initially temp=head
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
    # Here node class is used to create the node and nnode is its object
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        #self.Node=
    def append_Node(self,val):
        self.nnode=Node(val)
        if(self.head==None):
            self.head=self.nnode
            self.tail=self.nnode
        else:
            #temp=self.tail.next
            self.tail.next=self.nnode
            self.tail=self.tail.next
    def delete_last_Node(self):
        temp=self.head
        if(temp==None):
            print("No node is present")
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        self.tail=temp
    def delete_first_Node(self):
        temp=self.head
        if(temp==None):
            print("No node is present")
        else:
            temp=temp.next
            self.head.next=None
            self.head=temp
    def display(self):
        temp=self.head
        if(temp==None):
            print("No node is present")
        else:
            while(temp):
                print(temp.val)
                temp=temp.next
ll=LinkedList()
ll.append_Node(90)

        
    
    

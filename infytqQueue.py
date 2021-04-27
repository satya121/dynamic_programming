#enqueue : Enqueue meant for insertion , rear variable is used
#dequeue : Dequeue meant for deletion , front variable is used

class Queue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.data=[-1 for _ in range(size)]
    def enqueue(self,val):
        if(self.rear==self.size-1):
            print("Queue is full")
        else:
            if(self.rear==-1  and self.front==0 ):
                self.rear=0
                self.front=0
            else:
                self.rear+=1
            self.data[self.rear]=val
    def dequeue(self):
        if(self.rear==-1 and self.front==-1):
            print("Queue is empty")
        else:
            if(self.rear==self.front):
                self.rear=-1
                self.front=-1
            else:
                self.rear-=1
            self.data.pop(0)
    def display(self):
        if(self.rear==-1 and self.front==-1):
            print("Queue is empty")
        else:
            for i in self.data:
                print(i, end=' , ')
obj=Queue(3)
        

class Stack:
    def __init__(self,size,top=-1):
        self.size=size
        self.top=-1
        self.data=[]
        #self.data=[-1 for _ in range(size)]
    def push(self,val):
        print("size=",self.size,"top=",self.top)
        if(self.top==self.size-1):
            print("Stack Overflow")
        else:
            self.top+=1
            self.data.append(val)
            #self.data[self.top]=val
            print(self.data)
    def pop(self):
        if(self.top==-1):
            print("No element to pop")
        else:
            self.top-=1
            self.data.pop()
    def display(self):
        if(self.top==-1):
            print("Stack under flow")
        else:
            for i in self.data:
                print(i,end=' , ')

obj=Stack(2)
obj.push(59)
obj.push(50)
obj.pop()
obj.display()

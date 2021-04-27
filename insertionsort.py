class Sorting():
    def __init__(self,data):
        self.data=data
    def insertionsort(self):
        for i in range(1,len(self.data)):
            ele=self.data[i]
            for j in range(i-1,-1,-1):
                if(ele<self.data[j]):
                    self.data[j+1]=self.data[j]
                else:
                    self.data[j+1]=ele
                    break
            print(self.data)

data=[11,34,55,100,110,19,12,60,18,16]
obj=Sorting(data)
obj.insertionsort()

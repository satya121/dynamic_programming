l=[11,34,55,100,19,12,60,18,16,110]

'''
BubbleSort: In bubble sort the swapping is done in between two adjacent elements"
'''
class Sorting:
    def __init__(self,data):
        self.data=data
    def Bubble_sort(self):
        ps=0
        psc=1
        while(psc>0):
            psc=0
            for i in range(1,len(l)):
                if(l[i-1]>l[i]):
                    l[i],l[i-1]=l[i-1],l[i]
                    psc+=1
            ps+=1
            print("pass",ps,":-->",l)
data=list(map(int,input().split()))
obj=Sorting(data)
obj.Bubble_sort()


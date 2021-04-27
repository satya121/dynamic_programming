#binarysearch
class Search:
    def __init__(self,data,key):
        self.data=data
        self.key=key
    def binarysearch(self):
        l=0
        h=len(self.data)-1
        mid=(l+h)//2
        while(l<=h):
            if(key==self.data[mid]):
                print("key found")
                break
            elif(key<self.data[mid]):
                h=mid-1
            else:
                l=mid+1
            mid=(l+h)//2
            
        else:
            print("key not found")
key=int(input())
obj=Search([1,2,3,4,5,6,7,8,9],key)
obj.binarysearch()

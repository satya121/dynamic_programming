#binary_search using recursion
'''
def binary_search(low,high,l,k):
    if(low>high):
        return -1
    mid=(low+high)>>1
    if(l[mid]==k):
        return mid
    elif(l[mid]>k):
        res=binary_search(low,mid-1,l,k)
    elif(l[mid]<k):
        res=binary_search(mid+1,high,l,k)
    else:
        pass
    return res
    
for _ in range(int(input())):
    l=sorted(list(map(int,input().split())))
    
    k=int(input())
    print(binary_search(0,len(l)-1,l,k)) '''

#Binary search using normal function

def bin_search(l,h,l1,k):
    mid=(l+h)>>1
    while(l<=h):
        if(l1[mid]==k):
            return mid
        elif(l1[mid]>k):
            h=mid-1
        else:
            l=mid+1
        mid=(l+h)>>1
    return -1

for _ in range(int(input())):
    lst=sorted(list(map(int,input().split())))
    k1=int(input())
    print(bin_search(0,len(lst)-1,lst,k1))

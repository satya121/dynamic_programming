l=[11,34,55,100,110,19,12,60,18,16]
l1=[11,34,55,100,110,19,12,60,18,16]
print("using copy of list")
print("-----------------------------")
sort=l.copy()
for i in range(1,len(l)):
    a=i-1
    while(l[a]>l[i] and a>=0):
        a-= 
   tmp=l[a+1]
    l[a+1]=l[i]
    for j in range(a+2,i+1):
        l[j]=sort[j-1]
    sort=l.copy()
    print("pass-->",l)
print("-------------------------------")
print(l)
print("Using swapping")
print("-------------------------------")
for i in range(1,len(l1)):
    a=i
    while(l1[a-1]>l1[a]):
        l1[a],l1[a-1]=l1[a-1],l1[a]
        a-=1
        #print(l)
    print("pass-->",l1)



        
        
        

q=int(input())
for _ in range(q):
    n,x=input().split()
    n,x=int(n),int(x)
    l=list(map(int,input().split()))
    l=sorted(l)
    c=0
    for i in range(len(l)):
        j=i+1
        k=len(l)-1
        while(j<k):
            if(l[i]+l[j]+l[k])< x:
                k-=1
                c+=1
            elif(l[i]+l[j]+l[k])> x:
                k-=1
            else:
                j+=1
                k=len(l)-1
    print(c)

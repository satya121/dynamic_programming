def combinations(n,res):
    if(n==0):
        for i in res:
            print(i,end='')
        print()
    for i in range(1,n+1):
        res.append(i)
        print(res)
        combinations(n-i,res)
        res.pop()
        print("popped:",res)
        
        
    

n=int(input())
res=[]
combinations(n,res)

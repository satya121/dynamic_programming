# cook your dish here
#BFS
N=10000011
#in question it given to perform mod 100000


def BFS(sta,end,n,l):
    #create a queue with starting pt and stps to reach that(0)
    que=[[sta,0]]
    #create a reference array to check whether we visited that node or not
    arr=[0]*N
    arr[sta]=1
    res=0
    #keep iterating until your queue becomes empty
    while(len(que)!=0):
            c=0
            n1=que[0][0]
            steps=que[0][1]
            que.remove(que[0])
            for ele in l:
                res=(n1*ele)%1000000
                if(res==end):
                    return steps+1
                if(arr[res]!=1):
                    arr[res]=1
                    que.append([res,steps+1])
                if(res>end):
                    c+=1
                if(c==n):
                    return -1
                    
    return -1

sta=int(input("starting:"))
end=int(input("ending:"))
n=int(input("array length:"))
l=list(map(int,input().split()))
print(BFS(sta,end,n,l))

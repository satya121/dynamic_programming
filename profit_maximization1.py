n=int(input())
l=list(map(int,input().split()))
op_list=[i for i in l]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[j]%l[i]==0):
            op_list[j]=max(op_list[j],l[j]+op_list[i])
print(max(op_list))

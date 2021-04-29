'''
n=int(input())
l=list(map(int,input().split()))
res=[]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        tmp=sorted(l[i:j+1])
        t=[tmp[-1],tmp[-2]]
        if t not in res:
                   res.append(t)
print(len(res))
        
'''

n=int(input())
l=list(map(int,input().split()))
count=0
st=[]
for i in range(n):
    while(len(st)!=0 and st[-1]<l[i]):
        st.pop()
        count+=1
    if(st!=[]):
        count+=1
    st.append(l[i])
print(count)  

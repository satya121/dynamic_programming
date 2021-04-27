#Scalin algorithm ---> Advanced version of prefix sum
l=list(map(int,input().split()))
out=[]
sc=[0]*(len(l)+1)
for _ in range(int(input())):
    out.append(list(map(int,input().split())))
for i in out:
    sc[i[0]]+=i[-1]
    sc[i[1]+1]-=i[-1]
print(sc)

print(sc)
l[0]+=sc[0]
for i in range(1,len(l)):
    sc[i]+=sc[i-1]
    l[i]+=sc[i]
print(l)

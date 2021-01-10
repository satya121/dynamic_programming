N=20
sei=[i for i in range(N)]
temp=[2]*N
sei[0],sei[1]=0,0
def gen_sei():
    for i in range(2,N//2):
        if(sei[i]==i):
            for j in range(i+i,N,i):
                temp[j]-=1
                sei[j]=sei[j]//i
    print("sei=",sei)
    print("temp=",temp)
gen_sei()
a=int(input())
c=0
for i in range(2,a+1):
    if(temp[i]==0):
        c+=1
print(c)

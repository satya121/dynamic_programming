N=100001
sei=[i for i in range(N)]
sei[0],sei[1]=0,0
temp=[1]*N
def gen_seive():
    for i in range(2,int(N**0.5)+1):
        c=0
        #print(i)
        if(sei[i]==i):
            for j in range(i*i,N,i):
                if(sei[j]==j):
                    c+=1
                    sei[j]=i
        temp[i]=c
gen_seive()
print(sei)
q=int(input())
for _ in range(q):
    a=int(input())
    print(temp[a])

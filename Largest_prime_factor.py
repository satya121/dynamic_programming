N=1000001
seive=[i for i in range(N)]
def gen_seive():
    seive[0]=seive[1]=0
    for i in range(2,int(N**0.5)+1):
        if seive[i]==i:
            for j in range(i*i,N,i):
                seive[j]=i
gen_seive()
#print(seive)
q=int(input())
for _ in range(q):
    n=int(input())
    l=[seive[n]]
    a=n
    while(a!=1):
        a=a//seive[n]
        l.append(seive[a])
        n=a
    #print(l)
    print(max(l))

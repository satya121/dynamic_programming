s=input()
sub=set()
arr=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub.add(int(s[i:j]))
sub=sorted(list(sub))
if(sub[0]==0):
    sub.remove(0)
for i in sub:
    for j in range(int(i**0.5)+1):
        if(j*(j+1)==i):
            arr.append(i)

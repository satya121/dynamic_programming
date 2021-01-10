def minion_game(string):
    # your code goes here
    st=[]
    ke=[]
    s,k=0,0
    vow=['A','E','I','O','U']
    for i in range(len(string)):
        for j in range(len(string)-i):
            str=string[j:j+i+1]
            if(str[0] in vow):
                k+=1
            elif(str[0] not in vow):
                s+=1
    if(s>k):
        print("Stuart",s)
    elif(s==k):
        print("Draw")
    else:
        print("Kevin",k)   

s=input()
minion_game(s)

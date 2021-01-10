def binary_exponent(base,pow1):
    ans=1
    while(pow1!=1):
        if(pow1%2==0):
            ans*=base*base
            pow1=pow1//2
        else:
            ans*=base
            pow1-=1
    return ans
base=int(input())
pow1=int(input())
ans=binary_exponent(base,pow1)
print("binary_exponent=",ans)
def modular_Arithmetic(base,pow1):
    ans=1
    mod=((10**9)+7)
    while(pow1!=1):
        if(pow1%2==0):
            ans*=(base*base)%(mod)
            pow1=pow1//2
        else:
            ans*=(base)%(mod)
            pow1-=1
    return ans
ans=modular_Arithmetic(base,pow1)
print("Using_modulo=",ans)

def get_prime_factor(num):
    factor=[]
    pf=[]
    pfactor=[]
    c=0
    for i in range(1,num):
        if(num%i==0):
            factor.append(i)
    for j in factor:
        c=0
        for k in range(1,j+1):
            if(j%k==0):
                c+=1
        if(c==2):
            pf.append(j)
    v=0
    while(num>1):
        if(num%pf[v]==0):
            num=num/pf[v]
            pfactor.append(pf[v])
        else:
            v+=1
    return pfactor
print(get_prime_factor(60))
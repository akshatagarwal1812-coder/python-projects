str=input("enter the linee you want to code or decode")
a=input("enter the task you want to perform")
new=[]
if a=="code":
    list=str.split()
    for i in list:
        le=len(i)
        if(le<3):
           new.append(i[::-1])
        else:
            
            store=i[0]
            i=i[1:]
            ak= i+store
            new.append("aks"+ak+"jgf")
        print(new)
 

if a=="decode":
    list=str.split()
    for i in list:
        le=len(i)
        if(le<3):
           new.append(i[::-1])
        else:
            
            i=i[3:-3]
            store=i[-1]
            i=i[:-1]
            ak= store+i
            new.append(ak)
    print(new)
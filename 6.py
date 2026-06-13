
s1=0
s2=1
a=int(input("enter no of elements"))
l=[0,1]
c=2
while(c<a):
    sum=s1+s2
    l.append(sum)
    s1=s2
    s2=sum
    c+=1
print(l)
    
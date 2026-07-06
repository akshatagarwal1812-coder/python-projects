#LAMBDA FUNCTION
# import math as m
# def ak(fn,value):
#     return 12*fn(value)+8-2*fn(value)
# add=lambda x,y,z,a:(x+y+z+a)
# mult=lambda x,y,z:(x*y*z)
# dicid=lambda a,b,c,d:(a+b)/(c+d)
# sq=lambda s:m.sqrt(s)
# print(add(1,2,3,4))
# print(mult(2,3,4))
# print(dicid(6,1,3,4))
# print(sq(16))
# print(ak(sq,25))
#MAP FUNCTION
# l=[1,5,9,8,4,6,3,2,7]
# nel=[] 
# def sr(x):
#     return x*x  
# n=list(map(sr,l))
# print(n)
# #FILTER FUNCTION for odd and even using lambda function
# fl=list(filter(lambda x: x%2==0, l))
# fo=list(filter(lambda x: x%2!=0, l))
# print(fl)
# print(fo)
if __name__ == '__main__':
    n = int(input())
    out=0
    arr = list(map(int, input().split()))
    for i in range(0,n):
        if(2<=n<=10 and -100<=arr[i]<=100):
            arr.sort()
            out=arr[-2]
            c=-2
            for i in range(-1,-n):
                if(arr[i]>out):
                    break
                else:
                    c=c-1
                    out=arr[c]
                
            
print(out)
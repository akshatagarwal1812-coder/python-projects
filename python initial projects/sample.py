if __name__ == '__main__':
    N = int(input())
    li=[]
    for i in range(0,N):
        li.append(int(input("enter a element")))
    i=int(input())
    e=10
    li.insert(i,e)
    print(li)
    li.remove(e)
    print(li)
    li.append(e)
    print(li)
    li.sort()
    print(li)
    li.pop(-1)
    print(li)
    li.reverse()
    print(li)
    
# f=open("ak.txt", "r")
# i=0
# while True:
#     i=i+1
#     l=f.readline()
#     if not l :
#         break
#     m1=(l.split(",")[0])
#     m2=(l.split(",")[1])
#     m3=(l.split(",")[2])
#     print(f"marks of student{i} \n in maths={m1} \n in physics={m2} \n  in chemistry={m3} \n percentage={((int(m1)+int(m2)+int(m3))/300)*100}")
# f.close()
exist=0
pos=0
with open("practice.txt", "r") as f:
    def read_file():
        i=0
        while True:
            i=i+1
            line=f.readline()
            if not line:
                break
            nlne=line.replace("java", "python")
            print(nlne)
            if("learing" in line):
                global exist, pos
                exist=1
                pos=i

    read_file()
    if exist==1:
        print("yes")
        print(f"learning is present at line number {pos}")
    else:
        print("1")
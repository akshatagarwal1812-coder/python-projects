def palin(str):
    nstr=str.replace(" ","").lower()
    r=""
    for i in range(len(nstr)-1,-1,-1):
        r=r+nstr[i]
    return(r==nstr)
print(palin("A man a plan a canal Panama"))
def sort(string):
    l=string.split()
    nl=[]
    fl=[]
    for o in l:
        nl.append(o+(o.lower()))
    nl.sort(reverse=True)
    return ' '.join(nl)
print(sort("apple ORANGE banana"))
 
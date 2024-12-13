def newnumlist(n):
    list=[]
    pos=0
    for i in range(n):
        prod=0
        newlist=[]
        for i in range(1,6):
            prod=i*pos
            newlist.append(prod)
        pos+=1
        list.append(newlist)
    print(list)
newnumlist(5)
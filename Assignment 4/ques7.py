l=[1,2,3,4,5,6,7,8,9,10]
def cummlativelist(l):
    newlist=[]
    
    for i in range(0,len(l)):
        sum=0
        for j in range(0,i+1):
            sum+=l[j]
        newlist.append(sum)
    return newlist

newlist=cummlativelist(l)
for i in range(0,len(l)):
    print(f"{l[i]}  {newlist[i]}")
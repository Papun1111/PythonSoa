m=int(input("Enter rows:"))
n=int(input("Enter columns"))
l=[]

for i in range(0,m):
    newlist=[]
    for j in range(0,n):
        b=int(input("enter a number"))
        newlist.append(b)
    l.append(newlist)
print(l)
for i in l:
    for j in i:
        print(j,end=" ")
    print()
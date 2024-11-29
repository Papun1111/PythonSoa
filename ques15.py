import random
l=[]

for i in range(0,4):
    newlist=[]
    for j in range(0,4):
        b=random.randint(0,1)
        newlist.append(b)
    l.append(newlist)
print(l)
max = 0
rowidx = 0
for i in range(len(l)):
    count = 0
    for j in l[i]:
        if j == 1:
            count += 1
    if count > max:
        max = count
        rowidx = i + 1 

print(rowidx)


